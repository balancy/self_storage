from django import forms

from . import models


class FormPrettifyFieldsMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, obj in self.fields.items():
            if name != 'is_agree':
                obj.widget.attrs['class'] = f'form-control mt-3'
                obj.widget.attrs['id'] = name


class RentBoxForm(FormPrettifyFieldsMixin, forms.ModelForm):
    class Meta:
        model = models.RentalOrder
        fields = ('storage', 'size', 'duration')


class ApplicationForm(FormPrettifyFieldsMixin, forms.ModelForm):
    is_agree = forms.BooleanField(
        required=True,
        label='Соглашаюсь с условиями обработки персональных данных',
    )

    class Meta:
        model = models.Order
        fields = (
            'person_name',
            'phone_number',
            'passport_number',
            'birth_date',
        )


class StoreItemForm(FormPrettifyFieldsMixin, forms.ModelForm):
    class Meta:
        model = models.StoringOrder
        fields = ('storage', 'item', 'duration')
