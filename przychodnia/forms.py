from django import forms
from django.core.exceptions import ValidationError
from django.forms import models

from przychodnia.models import Owner


class AddOwnerForm(models.ModelForm):
    phone = forms.CharField(max_length=9, required=True)
    name = forms.CharField(max_length=30, required=True)
    address = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Owner
        fields = '__all__'


    def clean_phone(self):
        """
        Check if phone is only digits characters,
        it will be checked when is_valid() method is called
        """

        print("cleaning phone dayta")
        phone = self.cleaned_data.get('phone', 0)
        print(phone)

        if not phone.isnumeric():
            print("is not nbmeric")
            raise forms.ValidationError('Phone is not digit')

        return phone