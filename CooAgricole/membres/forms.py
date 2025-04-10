from django import forms
from django.contrib.auth.models import User
from .models import Membre

class InscriptionForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Membre
        fields = ['nom', 'email', 'phone_number'] 

    def save(self, commit=True):
        membre = super().save(commit=False)
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
        membre.user = user
        if commit:
            membre.save()
        return membre
