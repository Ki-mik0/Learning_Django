from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['name', 'percent']
        labels = {
            'name': 'Назва знижки або акції',
            'percent': 'Розмір знижки (%)',
        }