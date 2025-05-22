from django import forms
from .models import DeliveryHistory
from .models import ProductTransaction

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryHistory
        fields = ['petroleum_name', 'supplier', 'delivery_code', 'date_deliver', 'total_volume', 'total_price']
        widgets = {
            'date_deliver': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'date-deliver'
            }),
            'delivery_code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'delivery-code',
                'readonly': 'readonly'
            }),
            'petroleum_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'supplier': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'total_volume': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': 'required',
                'step': '0.01'
            }),
            'total_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': 'required',
                'step': '0.01'
            })
        }

class ProductTransactionForm(forms.ModelForm):
    class Meta:
        model = ProductTransaction
        fields = ['name', 'quantity', 'volume_liters', 'price_per_unit', 'total_price']