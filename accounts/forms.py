from django import forms
from django.utils.translation import gettext as _ 
from django.contrib.auth.models import User

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
            raise forms.ValidationError(_("Password and confirm password doen\'t match"))
        return cleaned_data

    def clean_username (self): 
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists(): 
            raise forms.ValidationError(_("Username is taken"))
        return username
    
    def clean_email (self): 
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists(): 
            raise forms.ValidationError(_("That email is being used"))
        return email

        
