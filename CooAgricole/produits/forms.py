from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['phone_number', 'amount']
        labels = {
            'phone_number': 'Numéro de téléphone Orange Money',
            'amount': 'Montant (en FCFA)',
        }
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Ex: 07000000'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Ex: 10000'}),
        }
        
