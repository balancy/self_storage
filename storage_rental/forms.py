from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

from . import models


class FormPrettifyFieldsMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, obj in self.fields.items():
            if name not in ('is_agree', 'is_processed'):
                obj.widget.attrs['class'] = f'form-control mt-3'
                obj.widget.attrs['id'] = name


class PromoFieldMixin(forms.Form):
    promocode = forms.CharField(label='Промокод', required=False)


class RentBoxForm(FormPrettifyFieldsMixin, PromoFieldMixin, forms.ModelForm):
    class Meta:
        model = models.RentalOrder
        fields = ('storage', 'size', 'duration', 'total_price', 'discount')
        widgets = {
            'total_price': forms.HiddenInput(),
            'discount': forms.HiddenInput(),
        }


class StoreItemForm(FormPrettifyFieldsMixin, PromoFieldMixin, forms.ModelForm):
    class Meta:
        model = models.StoringOrder
        fields = (
            'storage',
            'item',
            'quantity',
            'duration',
            'total_price',
            'discount',
        )
        widgets = {
            'total_price': forms.HiddenInput(),
            'discount': forms.HiddenInput(),
        }


class ApplicationForm(FormPrettifyFieldsMixin, forms.ModelForm):
    is_agree = forms.BooleanField(
        required=True,
        label='Соглашаюсь с условиями обработки персональных данных',
    )

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        years = (date.today() - birth_date).days / 365.25

        if years < 14:
            raise ValidationError(_("Возраст должен быть не меньше 14 лет!"))

        return birth_date

    class Meta:
        model = models.Order
        fields = (
            'person_name',
            'phone_number',
            'passport_number',
            'birth_date',
            'total_price',
        )
        widgets = {'total_price': forms.HiddenInput()}


class PaymentForm(FormPrettifyFieldsMixin, forms.ModelForm):
    card = forms.CharField(
        required=True,
        label='Номер карты',
        validators=[MinLengthValidator(16)],
    )

    def clean_is_processed(self):
        is_processed = self.cleaned_data['is_processed']

        if not is_processed:
            raise ValidationError(
                _(
                    'Вы должны заполнить все данные для оплаты (заглушка в '
                    'виде чекбокса)'
                )
            )

        return is_processed

    class Meta:
        model = models.Order
        fields = ('is_processed', 'total_price')
        widgets = {'total_price': forms.HiddenInput()}
