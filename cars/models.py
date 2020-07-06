from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Color(models.Model):
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.color

class Brand(models.Model): 
    brand = models.CharField(max_length=50)
    def __str__(self):
        return self.brand

class CarModel(models.Model):
    model = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.model

class Car(models.Model):
    
    class Color (models.TextChoices):
        BLACK = 'BK', _('Musta')
        WHITE = 'WT', _('Valkoinen')
        METALIC = 'MT', _('Metalli/Harma')
        
    class FuelType (models.TextChoices):
        DIESEL = 'DI', _('Diesel')
        PETROL = 'PE', _('Bensiini')
        ELECTRIC = 'EL', _('Sähkö')
        HYBRID = 'HY', _('Hybridi')
    
    class TransimissionType (models.TextChoices):
        AUTOMATIC = 'AU', _('Automaatti')
        MANUAL = 'MN', _('Manuaalli')

    class BodyType (models.TextChoices): 
        WAGON = 'WG', _('Farmari')
        SUV = 'SV', _('SUV')
        HATCHBACK = 'HB', _('Viistoperä')
        SEDAN = 'SD', _('Porrasperä')
    
    class UsePurpose (models.TextChoices):
        PRIVATE = 'PR', _('Omaan käyttöön')
        TAXI = 'TX', _('Taxi')

    #slug = models.SlugField(unique=True)
    color = models.CharField(max_length=20, choices=Color.choices, default=Color.WHITE)
    body_type = models.CharField(max_length=10, choices=BodyType.choices, default=BodyType.WAGON)
    fuel_type = models.CharField(max_length=10, choices=FuelType.choices, default=FuelType.PETROL)
    transmission = models.CharField(max_length=10, choices=TransimissionType.choices, default=TransimissionType.MANUAL)
    use_purpose = models.CharField(max_length=10, choices=UsePurpose.choices, default=UsePurpose.PRIVATE)
    ## seats from 0 24 passenger 
    seats = models.IntegerField(default=1, validators=[ MinValueValidator(0), MaxValueValidator(100)])
    damage_excess = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    ## day price for one day 
    price_day = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    ## one day price more then 7 day rentals 
    price_week = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    ## one day price more then 30 day rentals 
    price_month = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING)
    reg_number = models.CharField(max_length=10)
    issued_year = models.DateField(default=datetime.now)
    
    photo_1 = models.ImageField(upload_to='cars', blank=True)
    photo_2 = models.ImageField(upload_to='cars', blank=True)
    photo_3 = models.ImageField(upload_to='cars', blank=True)
    photo_4 = models.ImageField(upload_to='cars', blank=True)
    photo_5 = models.ImageField(upload_to='cars', blank=True)
    photo_6 = models.ImageField(upload_to='cars', blank=True)

    
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.reg_number
