from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from . import forms
from . import models
from .models import Storage


def serialize_place(place):
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.name,
                    "placeId": place.pk,
                    "detailsUrl": reverse('place_view', args=[place.pk])
                }
            }]
    }


def index(request):
    all_places = Storage.objects.all()
    context = {
        'all_places': [serialize_place(place) for place in all_places]
    }
    return render(request, "index.html", context)


def get_place_view(request, place_id):
    current_place = get_object_or_404(Storage, pk=place_id)

    context = {
        'title': current_place.name,
        # 'imgs': [image.image.url for image in current_place.images.all()],
        'lat': current_place.latitude,
        # 'description_short': current_place.description_short,
        # 'description_long': current_place.content,
        'coordinates': {
            'lat': current_place.latitude,
            'lng': current_place.longitude
        }
    }
    return JsonResponse(context, safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})


class RentalOrderView(CreateView):
    model = models.RentalOrder
    form_class = forms.RentBoxForm
    template_name = "storage_rental/rental_order.html"
    success_url = reverse_lazy('application_form')

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
    success_url = reverse_lazy('application_form')

    def form_valid(self, form):
        week_price = form.instance.item.week_storage_price
        month_price = form.instance.item.month_storage_price
        duration = form.instance.duration

        if duration < 4:
            total_price = duration * week_price
        else:
            total_price = (duration // 4) * month_price

        form.instance.total_price = total_price
        return super().form_valid(form)


def deposit_items(request):
    return HttpResponse("Deposit items page")


def application_form(request):
    return HttpResponse("Введите свои данные")
