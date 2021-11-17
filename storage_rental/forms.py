from django import forms

from . import models


class FormPrettifyFieldsMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, obj in self.fields.items():
            obj.widget.attrs['class'] = f'form-control mt-3'


class RentBoxForm(FormPrettifyFieldsMixin, forms.ModelForm):
    class Meta:
        model = models.RentalOrder
        fields = (
            'person_name',
            'phone_number',
            'passport_number',
            'birth_date',
            'storage',
            'size',
            'duration',
        )
