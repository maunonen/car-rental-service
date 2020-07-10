from django import forms 
from django.utils.translation import gettext as _ 

class EnrollForm ( forms.Form): 
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