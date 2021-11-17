# Generated by Django 3.2.9 on 2021-11-17 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage_rental', '0002_auto_20211117_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalorder',
            name='is_processed',
            field=models.BooleanField(default=False, verbose_name='обработан'),
        ),
        migrations.AddField(
            model_name='rentalorder',
            name='storage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='rental_orders', to='storage_rental.storage', verbose_name='склад'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storingorder',
            name='is_processed',
            field=models.BooleanField(default=False, verbose_name='обработан'),
        ),
    ]
