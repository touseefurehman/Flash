from django import forms
from .models import Rental
from .models import Rating

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'

