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
    template_name = "storage_rental/box_rental.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        base_price = form.instance.storage.base_price
        additional_price = form.instance.storage.additional_price
        size = form.instance.size
        duration = form.instance.duration
        total_price = duration * (base_price + additional_price * (size - 1))

        form.instance.total_price = total_price
        return super().form_valid(form)


def deposit_items(request):
    return HttpResponse("Deposit items page")
