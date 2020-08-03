from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, ProfileForm, ChangePassword

#import for mail notification 
from django.core.mail import send_mail, BadHeaderError
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
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
            #send email notification 
            # sedn notification to client 
            try:  
                context_client = {
                    'username' : username, 
                }
                # html message Version 
                html_message_client = render_to_string('email/client/register.html', context=context_client)
                # txt message VVersion
                subject_client = f'You have been successfully signed up!'
                plain_message_client = strip_tags(html_message_client)
                # send mail 
                mail.send_mail(
                    subject_client, 
                    plain_message_client, 
                    # from
                    settings.DEFAULT_FROM_EMAIL, 
                    # to recipients 
                    [email], 
                    html_message=html_message_client,
                    fail_silently=False,
                )
                print('Success Client')
            except BadHeaderError:
                print(BadHeaderError)
            
            # sen dnotification to admin 
            try: 
                # link to template 
                html_message = render_to_string('email/admin/register.html')
                # txt message VVersion
                subject = 'New user has been signed up'
                plain_message = strip_tags(html_message)
                mail.mail_admins(
                    subject, 
                    plain_message, 
                    fail_silently=False,
                    connection=None, 
                    html_message=html_message, 
                )
            except BadHeaderError: 
                print(BadHeaderError)
            
            messages.success(request, 'You now regestered and can log in')
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
                return redirect('rentals')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')

            #return redirect('dsahboard')
    else: 
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form })


def user_logout (request): 
    logout(request)
    messages.success(request, 'You have been successfully logged out') 
    return redirect('login')

def dashboard (request): 
    return render(request, 'accounts/dashboard.html')
  
@login_required(login_url='/accounts/login')
def delete_profile(request):        
    user = request.user
    email = user.email
    username = user.username
    user.is_active = False
    user.save()
    # send notification to client
    try:  
        context_client = {
            'username' : username, 
        }
        # html message Version 
        html_message_client = render_to_string('email/client/delete_profile.html', context=context_client)
        # txt message VVersion
        subject_client = f'Your account has been deleted successfully: {username}!'
        plain_message_client = strip_tags(html_message_client)
        # send mail 
        mail.send_mail(
            subject_client, 
            plain_message_client, 
            # from
            settings.DEFAULT_FROM_EMAIL, 
            # to recipients 
            [email], 
            html_message=html_message_client,
            fail_silently=False,
        )
        print('Success Client')
    except BadHeaderError:
        print(BadHeaderError)

    # send notification to admin     
    try: 
        # link to template 
        context = {
            'username' : username, 
            'email' : email
        }
        html_message = render_to_string('email/admin/delete_profile.html', context=context)
        # txt message VVersion
        subject = 'User profile has been deleted'
        plain_message = strip_tags(html_message)
        mail.mail_admins(
                        subject, 
                        plain_message, 
                        fail_silently=False,
                        connection=None, 
                        html_message=html_message, 
                    )
        print('Success Admin')
    except BadHeaderError: 
        print(BadHeaderError)
    finally: 
        print('Something went wrong')
    logout(request)
    messages.success(request, 'Profile successfully disabled.')
    return redirect('/accounts/login')


@login_required(login_url='/accounts/login')
def change_password(request): 
    if request.method == 'POST': 
        user = request.user
        form = PasswordChangeForm( user,  request.POST)
        if form.is_valid(): 
            messages.success(request, 'Your password was successfully updated!')
            form.save()
            return redirect('/accounts/profile')
        else : 
            content = { 'form' : form }
            return render(request, 'accounts/change_password.html', content)
    elif request.method == 'GET' : 
        form = PasswordChangeForm(user=request.user)
        content = { 'form' : form }
        return render(request, 'accounts/change_password.html', content)

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
