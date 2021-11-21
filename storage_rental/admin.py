from django.contrib import admin
from django.utils.html import format_html

from .models import Item, PromoСode, RentalOrder, Storage, StoringOrder


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(
            '<img src="{}" width="200px;" height="200px;" />'.format(
                obj.image.url
            )
        )

    list_display = (
        'id',
        'type',
        'image_tag',
        'week_storage_price',
        'month_storage_price',
    )

    ordering = ('type',)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(
            '<img src="{}" width="200px;" height="200px;" />'.format(
                obj.image.url
            )
        )

    list_display = (
        'id',
        'name',
        'image_tag',
        'address',
        'latitude',
        'longitude',
        'base_price',
        'additional_price',
    )

    ordering = ('name',)


@admin.register(RentalOrder)
class RentalOrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'person_name',
        'storage',
        'discount',
        'is_processed',
        'total_price',
    )

    ordering = ('person_name',)


@admin.register(StoringOrder)
class StoringOrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'person_name',
        'storage',
        'duration',
        'discount',
        'is_processed',
        'total_price',
    )

    ordering = ('person_name',)


@admin.register(PromoСode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'start_date', 'end_date', 'discount')

    ordering = ('code',)
