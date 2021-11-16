# Generated by Django 3.2.9 on 2021-11-16 18:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SKIS', 'Лыжи'), ('SNOWBOARD', 'Сноуборд'), ('BIKE', 'Велосипед'), ('TIRES', 'Шины')], default='SKIS', max_length=9, verbose_name='тип инвентаря')),
                ('image', models.ImageField(upload_to='media', verbose_name='Картинка')),
                ('week_storage_price', models.DecimalField(decimal_places=2, default=100, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='стоимость недельного хранения')),
                ('month_storage_price', models.DecimalField(decimal_places=2, default=300, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='стоимость месячного хранения')),
            ],
            options={
                'verbose_name': 'предмет инвентаря',
                'verbose_name_plural': 'предметы инвентаря',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='номер телефона')),
                ('passport_number', models.CharField(max_length=200, verbose_name='Номер паспорта')),
                ('birth_date', models.DateField(verbose_name='дата рождения')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='название')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='адрес')),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)], verbose_name='широта')),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=6, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='долгота')),
                ('base_price', models.DecimalField(decimal_places=2, default=599, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='базовая стоимость')),
                ('additional_price', models.DecimalField(decimal_places=2, default=150, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='добавочная стоимость')),
            ],
            options={
                'verbose_name': 'склад',
                'verbose_name_plural': 'склады',
            },
        ),
        migrations.CreateModel(
            name='StorageBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)], verbose_name='размер')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='boxes', to='storage_rental.storage', verbose_name='склад')),
            ],
            options={
                'verbose_name': 'бокс',
                'verbose_name_plural': 'боксы',
            },
        ),
        migrations.CreateModel(
            name='StoringOrder',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='storage_rental.order')),
                ('duration', models.PositiveSmallIntegerField(choices=[(1, '1 неделя'), (2, '2 недели'), (3, '3 недели'), (4, '1 месяц'), (8, '2 месяца'), (12, '3 месяца'), (16, '4 месяца'), (20, '5 месяцев'), (24, 'полгода')], default=1, verbose_name='срок хранения')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='общая стоимость хранения')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='storing_orders', to='storage_rental.item', verbose_name='инвентарь')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='storing_orders', to='storage_rental.storage', verbose_name='склад')),
            ],
            options={
                'verbose_name': 'заказ на хранение инвентаря',
                'verbose_name_plural': 'заказы на хранение инвентаря',
            },
            bases=('storage_rental.order',),
        ),
        migrations.CreateModel(
            name='RentalOrder',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='storage_rental.order')),
                ('duration', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)], verbose_name='срок аренды')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='общая стоимость аренды')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rental_orders', to='storage_rental.storagebox', verbose_name='бокс')),
            ],
            options={
                'verbose_name': 'заказ на аренду бокса',
                'verbose_name_plural': 'заказы на аренду боксов',
            },
            bases=('storage_rental.order',),
        ),
    ]
