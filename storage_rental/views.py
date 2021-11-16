from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Main page")


def rent_box(request):
    return HttpResponse("Rent box page")


def deposit_items(request):
    return HttpResponse("Deposit items page")
