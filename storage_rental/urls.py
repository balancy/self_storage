from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rent_box', views.rent_box, name='rent_box'),
    path('deposit_items', views.deposit_items, name='deposit_items'),
]
