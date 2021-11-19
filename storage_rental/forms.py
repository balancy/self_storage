from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

from . import models


class FormPrettifyFieldsMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, obj in self.fields.items():
            if name not in ('is_agree', 'is_processed', 'birth_date'):
                obj.widget.attrs['class'] = f'form-control mt-3'
                obj.widget.attrs['id'] = name


class RentBoxForm(FormPrettifyFieldsMixin, forms.ModelForm):
    class Meta:
        model = models.RentalOrder
        fields = ('storage', 'size', 'duration')


class ApplicationForm(FormPrettifyFieldsMixin, forms.ModelForm):
    is_agree = forms.BooleanField(
        required=True,
        label="Соглашаюсь с условиями обработки персональных данных",
    )

    class Meta:
        model = models.Order
        fields = (
            'person_name',
            'phone_number',
            'passport_number',
            'birth_date',
        )


class PaymentForm(FormPrettifyFieldsMixin, forms.ModelForm):
    card = forms.CharField(
        required=True,
        label="Номер карты",
        validators=[MinLengthValidator(16)],
    )

    def clean(self):
        if not self.cleaned_data['is_processed']:
            raise ValidationError(
                _(
                    'Вы должны заполнить все данные для оплаты (заглушка в '
                    'виде чекбокса)'
                )
            )

    class Meta:
        model = models.Order
        fields = ('is_processed',)


class StoreItemForm(FormPrettifyFieldsMixin, forms.ModelForm):
    class Meta:
        model = models.StoringOrder
        fields = ('storage', 'item', 'quantity', 'duration')
