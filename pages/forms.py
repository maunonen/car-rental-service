from django import forms
from django.utils.translation import gettext as _
import re


class ContactForm(forms.Form):
    
    name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'John'}
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder' : 'email@example.com'}
    ))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : '044558943'}
    ))
    message = forms.CharField(required=True, max_length=1000, widget=forms.Textarea(
        attrs={'class' : 'form-control', 'placeholder' : _('viesti')}
    ))

    def clean_phone_number(self):
        pattern = "^\d{6,14}$"
        phone_number = self.cleaned_data.get('phone_number')
        if not re.search(pattern, phone_number):
            raise forms.ValidationError( _("Väärä puhelinnumero"))
        return phone_number