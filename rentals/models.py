from django.db import models
from datetime import datetime, date
#import datetime
from django.utils.translation import gettext_lazy as _ 
from cars.models import *
from django.contrib.auth.models import User

# Create your models here.



class Rental(models.Model):
    
  ## ForeignKey optional fro User field 
  car = models.ForeignKey(Car, on_delete=models.DO_NOTHING) 
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True) 
  rental_start = models.DateField(default=date.today)
  rental_end = models.DateField(default=date.today)
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
  condition_approved = models.BooleanField(default=False)

  def __str__(self):
      return self.user + self.car

class Option(models.Model): 

  class Language (models.TextChoices):
    DEFAULT = '', _('Kieli')
    FINISH = 'fi', _('Suomi')
    RUSSIAN = 'ru', _('Venäjä')
    ENGLISH = 'en', _('Englanti')
    ESTONIAN = 'et', _('Viro')
    
  language = models.CharField(max_length=20, choices=Language.choices, default=Language.DEFAULT)
  name = models.CharField(max_length=50)
  price = models.DecimalField(default=0, max_digits=5, decimal_places=0)

  def __str__(self):
        return self.language +' - ' + self.name


class Specification(models.Model): 
  option = models.ForeignKey(Option, on_delete=models.DO_NOTHING) 
  rental = models.ForeignKey(Rental, on_delete=models.DO_NOTHING) 
  day = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(1)])
  price = models.DecimalField(default=0, max_digits=5, decimal_places=0)
  
  def __str__(self):
        return self.rental +' - ' + self.option
        