# Generated by Django 3.2.9 on 2021-11-20 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_rental', '0009_auto_20211120_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='скидка'),
        ),
    ]
