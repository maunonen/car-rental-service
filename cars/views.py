from django.shortcuts import render

# Create your views here.

def index(request): 
    return render(request, 'cars/cars.html') 

def car(request, car_id): 
    return render(request, 'cars/car.html') 