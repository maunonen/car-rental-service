from django import forms
from django.utils.translation import gettext as _ 
import datetime

class RentalForm (forms.Form): 

    rental_start = forms.DateField(widget=forms.widgets.DateInput(attrs={'class' : 'form-control', 'type': 'date'}))
    rental_end = forms.DateField(widget=forms.widgets.DateInput(attrs={'class' : 'form-control', 'type': 'date'}))
    
    first_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'John', 'aria-describedby' : "firstNamePrepend"}
    ))

    last_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Doe','aria-describedby' : "lastNamePrepend"}
    ))

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder' : 'email@example.com', 'aria-describedby' : "emailPrepend"}
    ))

    phone_number = forms.CharField(required=True, max_length=20, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : '044455555',  'aria-describedby' : "phoneNumberPrepend"}
    ))

    usage_place = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Helsinki' , 'aria-describedby' : "usagePlacePrepend"}
    ))

    pickup_location = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Helsinki' , 'aria-describedby' : "pickupLocationPrepend"}
    ))

    town = forms.CharField(required=True, max_length=20, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Vantaa', 'aria-describedby' : "townPrepend"}
    ))

    address = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Aleksanterinkatu 2 A 1', 'aria-describedby' : "addressPrepend"}
    ))

    postal_code = forms.CharField(required=True, max_length=20, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : '00100', 'aria-describedby' : "postalCodePrepend"}
    ))

    comments = forms.CharField(required=False, max_length=200, widget=forms.Textarea(
        attrs={ 'rows': 2,'class' : 'form-control', 'placeholder' : _('lisätietojä') , 'aria-describedby' : "commentsPrepend"}
    ))

    