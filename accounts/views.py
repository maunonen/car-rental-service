from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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
  
@login_required(login_url='/accounts/login')
def delete(request): 
    return redirect('login')

@login_required(login_url='/accounts/login')
def changePassword(request): 
    return redirect('login')


@login_required(login_url='/accounts/login')
def profile (request): 
    user = request.user
    if request.method == 'POST' or None : 
        form = ProfileForm(request.POST)
        if form.is_valid(): 
            ## get data from form 
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            
            town = form.cleaned_data.get('town')
            postal_code = form.cleaned_data.get('postal_code')
            address = form.cleaned_data.get('address')

            ## Save to user 
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.userprofile.phone_number = phone_number
            user.userprofile.town = town
            user.userprofile.postal_code = postal_code
            user.userprofile.address = address
            user.save()
            messages.success(request, 'You are succesfully updated profile information')
            return redirect('profile')
        else :
            context = {
                'form': form
            }
            return render(request, 'accounts/profile.html', context)
    else : 
        initial = {
            'last_name' : user.last_name ,
            'first_name' : user.first_name ,
            'email' : user.email ,
            'phone_number' : user.userprofile.phone_number if user.userprofile.phone_number else '' ,
            'town' : user.userprofile.town if user.userprofile.town else '' ,
            'postal_code' : user.userprofile.postal_code if user.userprofile.postal_code else '' ,
            'address' : user.userprofile.address if user.userprofile.address else '' ,
            }
        form = ProfileForm(initial)
        context = {
            'form' : form
        }

        return render(request, 'accounts/profile.html', context)
