from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Storage(models.Model):
    name = models.CharField(
        'название',
        max_length=100,
        blank=True,
    )

    address = models.CharField(
        'адрес',
        max_length=200,
        blank=True,
    )

    latitude = models.DecimalField(
        'широта',
        max_digits=6,
        decimal_places=3,
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )

    longitude = models.DecimalField(
        'долгота',
        max_digits=6,
        decimal_places=3,
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )

    base_price = models.DecimalField(
        'базовая стоимость',
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=599,
    )

    additional_price = models.DecimalField(
        'добавочная стоимость',
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=150,
    )

    image = models.ImageField('Картинка', upload_to='media', null=True)

    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'склады'

    def __str__(self):
        return f'{self.name}, {self.address}'


class Item(models.Model):
    class ItemType(models.TextChoices):
        SKIS = 'SKIS', _('Лыжи')
        SNOWBOARD = 'SNOWBOARD', _('Сноуборд')
        BIKE = 'BIKE', _('Велосипед')
        TIRES = 'TIRES', _('Шины')

    type = models.CharField(
        max_length=9,
        choices=ItemType.choices,
        default=ItemType.SKIS,
        verbose_name='тип инвентаря',
    )

    image = models.ImageField('Картинка', upload_to='media')

    week_storage_price = models.DecimalField(
        'стоимость недельного хранения',
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=100,
    )

    month_storage_price = models.DecimalField(
        'стоимость месячного хранения',
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=300,
    )

    class Meta:
        verbose_name = 'предмет инвентаря'
        verbose_name_plural = 'предметы инвентаря'

    def __str__(self):
        return self.type


class Order(models.Model):
    person_name = models.CharField('ФИО', max_length=200, blank=True)
    phone_number = PhoneNumberField('номер телефона', blank=True)
    passport_number = models.CharField(
        'Номер паспорта',
        max_length=20,
        blank=True,
    )
    birth_date = models.DateField('дата рождения', blank=True, null=True)


class RentalOrder(Order):
    class Duration(models.IntegerChoices):
        ONE_MONTH = '1', _('1 месяц')
        TWO_MONTHS = '2', _('2 месяца')
        THREE_MONTHS = '3', _('3 месяца')
        FOUR_MONTHS = '4', _('4 месяца')
        FIVE_MONTHS = '5', _('5 месяцев')
        SIX_MONTHS = '6', _('6 месяцев')
        SEVEN_MONTHS = '7', _('7 месяцев')
        EIGHT_MONTHS = '8', _('8 месяцев')
        NINE_MONTHS = '9', _('9 месяцев')
        TEN_MONTHS = '10', _('10 месяцев')
        ELEVEN_MONTHS = '11', _('11 месяцев')
        TWELVE_MONTHS = '12', _('1 год')

    duration = models.PositiveSmallIntegerField(
        'срок хранения',
        choices=Duration.choices,
        default=Duration.ONE_MONTH,
    )

    storage = models.ForeignKey(
        Storage,
        related_name='rental_orders',
        verbose_name='склад',
        on_delete=models.PROTECT,
    )

    size = models.PositiveSmallIntegerField(
        'размер бокса в м²',
        validators=[MaxValueValidator(20), MinValueValidator(1)],
        default=1,
    )

    total_price = models.DecimalField(
        'общая стоимость аренды',
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    is_processed = models.BooleanField(
        'обработан',
        default=False,
    )

    class Meta:
        verbose_name = 'заказ на аренду бокса'
        verbose_name_plural = 'заказы на аренду боксов'

    def __str__(self):
        return f'Заказ на аренду бокса размером {self.size} кв. м. на {self.duration} месяцев'


class StoringOrder(Order):
    class Duration(models.IntegerChoices):
        ONE_WEEK = '1', _('1 неделя')
        TWO_WEEKS = '2', _('2 недели')
        THREE_WEEKS = '3', _('3 недели')
        ONE_MONTH = '4', _('1 месяц')
        TWO_MONTHS = '8', _('2 месяца')
        THREE_MONTHS = '12', _('3 месяца')
        FOUR_MONTHS = '16', _('4 месяца')
        FIVE_MONTHS = '20', _('5 месяцев')
        SIX_MONTHS = '24', _('полгода')

    storage = models.ForeignKey(
        Storage,
        related_name='storing_orders',
        verbose_name='склад',
        on_delete=models.PROTECT,
    )

    item = models.ForeignKey(
        Item,
        related_name='storing_orders',
        verbose_name='инвентарь',
        on_delete=models.PROTECT,
    )

    duration = models.PositiveSmallIntegerField(
        'срок хранения',
        choices=Duration.choices,
        default=Duration.ONE_WEEK,
    )

    total_price = models.DecimalField(
        'общая стоимость хранения',
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    is_processed = models.BooleanField(
        'обработан',
        default=False,
    )

    class Meta:
        verbose_name = 'заказ на хранение инвентаря'
        verbose_name_plural = 'заказы на хранение инвентаря'

    def __str__(self):
        return f'Заказ на хранение {self.item} на {self.duration} месяцев'
