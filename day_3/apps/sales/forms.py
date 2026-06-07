from django import forms
from .models import Sales

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['product', 'quantity', 'total_amount']
        labels = {
            'product': 'Оберіть товар',
            'quantity': 'Кількість',
            'total_amount': 'Загальна сума',
        }