# Generated by Django 3.2.9 on 2021-11-19 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_rental', '0005_auto_20211119_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='storingorder',
            name='quantity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='количество'),
        ),
    ]
