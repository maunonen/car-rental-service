#import json 
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from  .models import CarModel, Brand, Car
from pages.models import Page
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .forms import SearchForm

# Create your views here.

def search (request): 
    cars = Car.objects.all()
    form = SearchForm(request.GET)
    if form.is_valid(): 
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
        
        rental_start_date = datetime.datetime.strptime(rental_start, '%Y-%m-%d')
        rental_end_date = datetime.datetime.strptime(rental_end, '%Y-%m-%d')
        interval = (rental_end_date - rental_start_date).days

        for car in cars: 
            # if interval > 7 total_price = interval * week price 
            if interval > 7  and interval < 30 : 
                car_rental_price = car.price_week 
            # if interval < 7 total_price = interval * day price 
            elif interval <= 7: 
                car_rental_price = car.price_day
            # if interval > 30 total_price = interval * month_price 
            elif interval >= 30: 
                car_rental_price = car.price_month
            
            # count rental_price 
            if car_rental_price: 
                total_sum = interval * car_rental_price
                car.total_sum = total_sum
                car.interval = interval
            else : 
                car.total_sum = None
        
        context = {
            'cars' : cars, 
            'form' : form, 
            'rental_start' : rental_start_date, 
            'rental_end' : rental_end_date
        }
        return render(request, 'cars/cars.html', context)
    else:
        context = {
            'form' : form
        }
        return render(request, 'cars/cars.html', context)

    context = {
        'cars' : cars, 
        'form' : form, 
    }
    return render(request, 'cars/cars.html', context)

def index(request): 
    
    content = Page.objects.all()
    ## 1. default page name 
    pageName = 'CL'
    ##  2. default language
    pageLang = 'fi'

    ##  3. check current language 
    if request.LANGUAGE_CODE: 
        pageLang = request.LANGUAGE_CODE
    
    ## 4. get content from database by page name and language
    try :
        content = content.filter(page_name__iexact=pageName, page_lang__iexact=pageLang).get()
    # Object  not found  
    except ObjectDoesNotExist:
        content = ''
        
    # Multiply Object were found 
    except MultipleObjectsReturned: 
        content = ''
    
    if not content: 
        content = ''

    form = SearchForm()
    context = {
        'content' : content, 
        'form' : form
    }
    return render(request, 'cars/cars.html', context)

def private(request): 
    #cars = Car.objects.all().filter(use_purpose="PR")
    form = SearchForm()
    context = {
        #'cars' : cars, 
        'form' : form
    }
    return render(request, 'cars/cars.html', context)

def business(request): 
    form = SearchForm()
    #cars = Car.objects.all().filter(use_purpose="TX")
    context = {
        #'cars' : cars, 
        'form' : form
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
    