#from django import forms, ModelForm
from django import forms
from django.utils.translation import gettext as _ 
from django.contrib.auth.models import User

class ProfileForm(forms.Form): 
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control form-control', 'placeholder' : 'email@example.com'}
    ))
    first_name = forms.CharField(required=False, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'John', 'aria-describedby' : "firstNamePrepend"}
    ))
    last_name = forms.CharField(required=False, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Doe','aria-describedby' : "lastNamePrepend"}
    ))
    phone_number = forms.CharField(required=False, max_length=20, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : '044455555',  'aria-describedby' : "phoneNumberPrepend"}
    ))
    town = forms.CharField(required=False, max_length=20, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Vantaa', 'aria-describedby' : "townPrepend"}
    ))
    postal_code = forms.CharField(required=False, max_length=20, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : '00100', 'aria-describedby' : "postalCodePrepend"}
    ))
    address = forms.CharField(required=False, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Aleksanterinkatu 2 A 1', 'aria-describedby' : "addressPrepend"}
    ))



class LoginForm(forms.Form): 
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder' : 'username'}
    ))
    password = forms.CharField( required=True, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control form-control-lg', 'type' : 'password'}
    ))


class RegisterForm(forms.Form): 

    username = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control form-control-lg', 'placeholder' : 'John'}
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder' : 'email@example.com'}
    ))
    password = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control form-control-lg', 'type' : 'password'}
    ))
    confirm_password = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={'class' : 'form-control form-control-lg', 'type' : 'password'}
    ))
    
    def clean (self): 
        cleaned_data = super().clean()
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password : 
            raise forms.ValidationError(_("Salasana ja vahvista salasana eivät täsmää"))
        return cleaned_data

    def clean_username (self): 
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists(): 
            raise forms.ValidationError(_("Käyttäjätunnus on jo olemassa"))
        return username
    
    def clean_email (self): 
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists(): 
            raise forms.ValidationError(_("Sähköpostiosoite on jo olemassa")) 
        return email

        
