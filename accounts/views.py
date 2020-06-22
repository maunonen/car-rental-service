from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout

# Create your views here.

def register (request): 
    if request.method == 'POST' or None :
        form =  RegisterForm(request.POST)
        if form.is_valid(): 
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, 'You now regestered and can login')
            return redirect('login')
    else: 
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form })

def login (request): 
    if request.method == 'POST' or None :
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password) 
            if user is not None: 
                auth.login(request, user)
                messages.success(request, 'You a now logged in')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')

            #return redirect('dsahboard')
    else: 
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form })


def user_logout (request): 
    logout(request)
    return redirect('login')

def dashboard (request): 
    return render(request, 'accounts/dashboard.html')
  