from django.contrib import admin

from .models import Item, RentalOrder, Storage, StorageBox, StoringOrder


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = 'type', 'week_storage_price', 'month_storage_price'


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'latitude',
        'longitude',
        'base_price',
        'additional_price',
    )


@admin.register(StorageBox)
class StorageBoxAdmin(admin.ModelAdmin):
    list_display = ('storage', 'size')


@admin.register(RentalOrder)
class RentalOrderAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'box', 'duration', 'total_price')


@admin.register(StoringOrder)
class StoringOrderAdmin(admin.ModelAdmin):
    list_display = (
        'person_name',
        'storage',
        'item',
        'duration',
        'total_price',
    )
