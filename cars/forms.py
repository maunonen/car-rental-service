from django import forms
from django.forms import ModelForm
from .models import Car, CarModel, Brand


class SearchForm(ModelForm):
    
    rental_start = forms.DateField(widget=forms.widgets.DateInput(attrs={'class' : 'form-control form-control-sm', 'type': 'date'}))
    rental_end = forms.DateField(widget=forms.widgets.DateInput(attrs={'class' : 'form-control form-control-sm', 'type': 'date'}))
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
        self.fields['rental_start'].required = False
        self.fields['rental_end'].required = False
        self.fields['transmission'].required = False
        self.fields['use_purpose'].required = False