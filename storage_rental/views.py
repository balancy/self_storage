from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
from . import models


def index(request):
    return HttpResponse("Main page")


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
