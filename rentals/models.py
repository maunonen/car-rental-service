from django.db import models
from datetime import datetime, date
#import datetime
from django.utils.translation import gettext_lazy as _ 
from cars.models import *
from django.contrib.auth.models import User

# Create your models here.

class Rental(models.Model):
    
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING) 
    ## ForeignKey optional fro User field 
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True) 
    rental_start = models.DateField(default=date.today)
    rental_end = models.DateField(default=date.today)
    #pickup_time = models.TimeField(auto_now=False, auto_now_add=False)
    #return_time = models.DateField(default=datetime.now)
    rental_sum = models.DecimalField(max_digits=5, decimal_places=2)
    
    first_name = models.CharField( max_length=50)    
    last_name = models.CharField(max_length=50, default='John')    
    email = models.EmailField( max_length=254)   
    phone_number = models.CharField( max_length=20)    
    usage_place = models.CharField( max_length=50)    
    pickup_location = models.CharField( max_length=50)    
    town = models.CharField( max_length=50)    
    address = models.CharField( max_length=200)    
    postal_code = models.CharField( max_length=10)  
    comments = models.TextField( max_length=200)

    def __str__(self):
        return self.user + self.car

        