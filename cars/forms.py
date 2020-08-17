from django import forms
from django.forms import ModelForm
from .models import Car, CarModel, Brand
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from django.utils import timezone
import pytz 

class SearchForm(ModelForm):
    
    rental_start = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'class' : 'form-control form-control-sm', 'type': 'date'}))
    rental_end = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'class' : 'form-control form-control-sm', 'type': 'date'}))
    class Meta: 
        model = Car
        fields = ['car_type', 'fuel_type', 'transmission', 'use_purpose']
        widgets = {
        'car_type': forms.Select(
            attrs={
                'class': 'form-control form-control-sm'
                }
            ),
        'fuel_type': forms.Select(
            attrs={
                'class': 'form-control form-control-sm'
                }
            ),
        'transmission': forms.Select(
            attrs={
                'class': 'form-control form-control-sm'
                }
            ),
        'use_purpose': forms.Select(
            attrs={
                'class': 'form-control form-control-sm'
                }
            ),
        }
    
    # setting up required to False
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['car_type'].required = False
        self.fields['fuel_type'].required = False
        self.fields['transmission'].required = False
        self.fields['use_purpose'].required = False

    def clean(self):
        
        # cleaned data
        cleaned_data = super().clean()
        # get current date
        current_date = datetime.date.today()
        # get start and end day
        rental_start = cleaned_data.get("rental_start").replace(tzinfo=None).date()
        rental_end = cleaned_data.get("rental_end").replace(tzinfo=None).date()
        
        # Error rental start greater than rental end 
        if rental_start > rental_end:
            raise forms.ValidationError(_("Palautuspäivä ei voi olla pieni kuin  noutopäivä."), code='invalid')
        # Error if rental_start is equal to rental_end 
        if rental_start == rental_end: 
            raise forms.ValidationError(_("Palautuspäivä ei voi yhtä suuri kuin noutopäivä."), code='invalid')
        # Error if rental_start date and rental_end less than current date 
        if rental_start < current_date or rental_end < current_date:
            raise forms.ValidationError(_("Palautuspäivä noutopäivä ei voi olla pienempi kuin kuin nykyinen päivä"), code='invalid')
        
        return cleaned_data
