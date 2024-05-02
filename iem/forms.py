        
from django import forms
from .models import item
 

class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['title', 'category', 'daily', 'weekly', 'monthly', 'market_value', 'quantity', 'mini_rental_days', 'location', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),  
            'location': forms.Textarea(attrs={'rows': 2}),   
        }
from django.contrib import admin
from .models import item

admin.site.register(item)

