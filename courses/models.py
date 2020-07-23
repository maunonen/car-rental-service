from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

class Course (models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField(max_length=50)
    full_description = models.TextField(max_length=500)
    course_start = models.DateField(default=date.today)
    course_end = models.DateField(default=date.today)
    course_price = models.DecimalField(max_digits=6, decimal_places=2)
    course_image = models.ImageField(upload_to='cars', blank=True)
    is_published = models.BooleanField(default=True)
    course_duration = models.IntegerField(default=30, 
        validators=[ MaxValueValidator(365), MinValueValidator(0)]
    )
    def __str__(self):
        return self.title