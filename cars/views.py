from django.shortcuts import render
from  .models import CarModel, Brand, Car
from pprint import pprint
import json 
from django.http import HttpResponseRedirect
from .forms import SearchForm
import datetime

# Create your views here.

def search (request): 
    cars = Car.objects.all()
    search_form = SearchForm(request.GET)
    #fuel_type
    if 'fuel_type' in request.GET: 
        fuel_type = request.GET['fuel_type']
        if fuel_type : 
            cars = cars.filter(fuel_type__iexact=fuel_type)         
    #transmission
    if 'transmission' in request.GET: 
        transmission = request.GET['transmission']
        if transmission : 
            cars = cars.filter(transmission__iexact=transmission)         
    # use_purpose
    if 'use_purpose' in request.GET: 
        use_purpose = request.GET['use_purpose']
        if use_purpose : 
            cars = cars.filter(use_purpose__iexact=use_purpose)         
    # use_purpose
    if 'car_type' in request.GET: 
        car_type = request.GET['car_type']
        if car_type :
            cars = cars.filter(car_type__iexact=car_type)
    # rental_start
    if 'rental_start' and 'rental_end' in request.GET: 
        rental_start = request.GET['rental_start']
        rental_end = request.GET['rental_end']
        if rental_start and rental_end:
            cars = cars.exclude(rental__rental_start__gte=rental_start, rental__rental_end__lte=rental_end)
    # count interval count 
        # get price for week 
        # month 
        # day 

    # how to add value to query set 

    rental_start_date = datetime.datetime.strptime(rental_start, '%Y-%m-%d')
    rental_end_date = datetime.datetime.strptime(rental_end, '%Y-%m-%d')
    interval = (rental_end_date - rental_start_date).days


    for car in cars: 
        # if interval > 7 total_price = interval * week price 
        if interval > 7  and interval < 30 : 
            car_rentla_price = car.price_week 
        # if interval < 7 total_price = interval * day price 
        elif interval <= 7: 
            car_rentla_price = car.price_day
        # if interval > 30 total_price = interval * month_price 
        elif interval > 30: 
            car_rentla_price = car.price_month
        
        # count rental_price 
        if car_rentla_price: 
            total_sum = interval * car_rentla_price
            car.total_sum = total_sum
            car.interval = interval
        else : 
            car.total_sum = None
        print(car.total_sum)

    context = {
        'cars' : cars, 
        'search_form' : search_form

    }
    return render(request, 'cars/cars.html', context)

def index(request): 
    #cars = Car.objects.all()
    search_form = SearchForm()
    context = {
        #'cars' : cars, 
        'search_form' : search_form
    }
    return render(request, 'cars/cars.html', context)

def private(request): 
    #cars = Car.objects.all().filter(use_purpose="PR")
    search_form = SearchForm()
    context = {
        #'cars' : cars, 
        'search_form' : search_form
    }
    return render(request, 'cars/cars.html', context)

def business(request): 
    search_form = SearchForm()
    #cars = Car.objects.all().filter(use_purpose="TX")
    context = {
        #'cars' : cars, 
        'search_form' : search_form
    }
    return render(request, 'cars/cars.html', context)


def car(request, car_id): 
    if car_id:
        car = Car.objects.get(pk=car_id)
        if not car: 
            return HttpResponseRedirect('/cars')
        else : 
            context = {
                'car' : car
            }
            return render(request, 'cars/car.html', context=context)
    else: 
        return HttpResponseRedirect('/cars')
    