from django.shortcuts import render
from  .models import CarModel, Brand, Car
from pprint import pprint
import json 
from django.http import HttpResponseRedirect

# Create your views here.

def index(request): 
    cars = Car.objects.all()
    context = {
        'cars' : cars
    }
    return render(request, 'cars/cars.html', context)

def private(request): 
    cars = Car.objects.all().filter(use_purpose="PR")
    context = {
        'cars' : cars
    }
    return render(request, 'cars/cars.html', context)

def business(request): 
    cars = Car.objects.all().filter(use_purpose="TX")
    context = {
        'cars' : cars
    }
    return render(request, 'cars/cars.html', context)


def car(request, car_id): 
    if car_id:
        car = Car.objects.get(pk=car_id)
        print('Car objject', car)
        if not car: 
            return HttpResponseRedirect('/cars')
        else : 
            context = {
                'car' : car
            }
            return render(request, 'cars/car.html', context=context)
    else: 
        return HttpResponseRedirect('/cars')
    