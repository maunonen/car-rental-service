from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
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
    
    class FuelType (models.TextChoices):
        DIESEL = 'DI', _('Diesel')
        PETROL = 'PE', _('Petrol')
        ELECTRIC = 'EL', _('Electric')
        HYBRID = 'HY', _('Hybrid')
    
    class TransimissionType (models.TextChoices):
        AUTOMATIC = 'AU', _('Automatic')
        MANUAL = 'MN', _('Manual')

    class BodyType (models.TextChoices): 
        WAGON = 'WG', _('Wagon')
        SUV = 'SV', _('SUV')
        HATCHBACK = 'HB', _('Hatchback')
        SEDAN = 'SD', _('Sedan')

    
    body_type = models.CharField(max_length=10, choices=BodyType.choices, default=BodyType.WAGON)
    fuel_type = models.CharField(max_length=10, choices=FuelType.choices, default=FuelType.PETROL)
    transmission = models.CharField(max_length=10, choices=TransimissionType.choices, default=TransimissionType.MANUAL)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
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
