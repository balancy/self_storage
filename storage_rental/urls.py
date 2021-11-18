from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rent_box', views.RentalOrderView.as_view(), name='rent_box'),
    path(
        'deposit_items',
        views.StoringOrderView.as_view(),
        name='deposit_items',
    ),
    path(
        'application/<int:pk>/',
        views.ApplicationView.as_view(),
        name='application',
    ),
    path('payment', views.payment, name='payment'),
]
