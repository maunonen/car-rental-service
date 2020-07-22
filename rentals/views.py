from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _ 
from django.contrib import messages
from .forms import RentalForm
from datetime import date

from .models import Rental
from cars.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login')
def index (request): 
    user = request.user
    rentals = Rental.objects.filter(user=user)
    context = {     
        'rentals' : rentals
    }
    return render(request, 'rentals/rentals.html', context )

def add(request, car_id): 
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST' or None: 
        form = RentalForm(request.POST)
        if form.is_valid():
            rental_start = form.cleaned_data.get('rental_start')
            rental_end = form.cleaned_data.get('rental_end')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            usage_place = form.cleaned_data.get('usage_place')
            pickup_location = form.cleaned_data.get('pickup_location')
            town = form.cleaned_data.get('town')
            address = form.cleaned_data.get('address')
            postal_code = form.cleaned_data.get('postal_code')
            comments = form.cleaned_data.get('comments')
            rental = Rental(
                car = car, 
                rental_start = rental_start, 
                rental_end = rental_end, 
                first_name = first_name,  
                last_name = last_name,  
                email = email, 
                phone_number = phone_number, 
                usage_place = usage_place, 
                pickup_location = pickup_location, 
                town = town, 
                address = address, 
                postal_code = postal_code, 
                comments = comments, 
                rental_sum = 123
            )
            if request.user.is_authenticated:
                rental.user = request.user
            rental.save()
            messages.success(request, 'Thank for rental car')
            return redirect('cars')
    else: 
        if request.user.is_authenticated:
            user = request.user
            today = date.today()
            initial = {
                'rental_start' : today,
                'rental_end' : today,
                'usage_place' : 'Helsinki',
                'pickup_location' : 'Helsinki',
                'comments' : '', 
                'last_name' : user.last_name ,
                'first_name' : user.first_name ,
                'email' : user.email ,
                'phone_number' : user.userprofile.phone_number if user.userprofile.phone_number else '' ,
                'town' : user.userprofile.town if user.userprofile.town else '' ,
                'postal_code' : user.userprofile.postal_code if user.userprofile.postal_code else '' ,
                'address' : user.userprofile.address if user.userprofile.address else '' ,
            }
            form = RentalForm(initial)
            #form = RentalForm()
        else :
            form = RentalForm()
        context = {
            'car' : car, 
            'form' : form
        }
        return render(request, 'rentals/rental.html', context )
    