from django.contrib import admin
from django.utils.html import format_html

from .models import Item, RentalOrder, Storage, StoringOrder


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(
            '<img src="{}" height="200px;" />'.format(obj.image.url)
        )

    list_display = (
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
            '<img src="{}" height="200px;" />'.format(obj.image.url)
        )

    list_display = (
        'name',
        'image_tag',
        'address',
        'latitude',
        'longitude',
        'base_price',
        'additional_price',
    )

    ordering = ('name', 'latitude', 'longitude')


@admin.register(RentalOrder)
class RentalOrderAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'storage',
        'size',
        'duration',
        'is_processed',
        'total_price',
    )


@admin.register(StoringOrder)
class StoringOrderAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'storage',
        'item',
        'duration',
        'is_processed',
        'total_price',
    )
