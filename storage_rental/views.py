from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
import simplejson as json

from . import forms
from . import models
from .models import Item, Storage, PromoСode


def serialize_place(place):
    return {
        "name": place.name,
        "address": place.address,
        "image": place.image.url,
        "base_price": place.base_price,
        "additional_price": place.additional_price,
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude],
                },
                "properties": {
                    "full_name": f"{place.name}, {place.address}",
                    "placeId": place.pk,
                },
            }
        ],
    }


def index(request):
    all_places = Storage.objects.all()
    context = {'all_places': [serialize_place(place) for place in all_places]}
    return render(request, "storage_rental/index.html", context)


def serialize_queryset(model, field='id'):
    return {
        record[field]: {
            key: value
            for key, value in record.items()
            if key not in [field, '_state']
        }
        for record in [instance.__dict__ for instance in model.objects.all()]
    }


class RentalOrderView(CreateView):
    model = models.RentalOrder
    form_class = forms.RentBoxForm
    template_name = "storage_rental/rental_order.html"

    def get_success_url(self) -> str:
        return reverse_lazy('application', kwargs={'pk': self.object.id})

    def get_context_data(self, *args, **kwargs):
        context = super(RentalOrderView, self).get_context_data(
            *args, **kwargs
        )

        context['promocodes'] = json.dumps(
            serialize_queryset(PromoСode, field='code'),
            default=str,
        )
        context['storages'] = json.dumps(
            serialize_queryset(Storage),
            use_decimal=True,
        )

        return context

    def form_valid(self, form):
        base_price = form.instance.storage.base_price
        additional_price = form.instance.storage.additional_price
        size = form.instance.size
        duration = form.instance.duration
        total_price = duration * (base_price + additional_price * (size - 1))

        form.instance.total_price = total_price
        return super().form_valid(form)


class StoringOrderView(CreateView):
    model = models.StoringOrder
    form_class = forms.StoreItemForm
    template_name = "storage_rental/storing_order.html"

    def get_success_url(self) -> str:
        return reverse_lazy('application', kwargs={'pk': self.object.id})

    def get_context_data(self, *args, **kwargs):
        context = super(StoringOrderView, self).get_context_data(
            *args, **kwargs
        )

        context['promocodes'] = json.dumps(
            serialize_queryset(PromoСode, field='code'),
            default=str,
        )
        context['items'] = json.dumps(
            serialize_queryset(Item),
            use_decimal=True,
        )

        return context

    def form_valid(self, form):
        week_price = form.instance.item.week_storage_price
        month_price = form.instance.item.month_storage_price
        duration = form.instance.duration
        quantity = form.instance.quantity

        if duration < 4:
            total_price = quantity * duration * week_price
        else:
            total_price = quantity * (duration // 4) * month_price

        form.instance.total_price = total_price
        return super().form_valid(form)


class ApplicationView(UpdateView):
    model = models.Order
    form_class = forms.ApplicationForm
    template_name = "storage_rental/application.html"

    def get_success_url(self) -> str:
        return reverse_lazy('payment', kwargs={'pk': self.object.id})


class PaymentView(UpdateView):
    model = models.Order
    form_class = forms.PaymentForm
    template_name = "storage_rental/payment.html"
    success_url = reverse_lazy("thanks")


def thanks(request):
    return render(request, "storage_rental/thanks.html")
