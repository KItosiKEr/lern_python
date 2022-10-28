from tabnanny import verbose
from django.db import models
from django.forms import CharField
from jinja2 import ChainableUndefined


class Food(models.Model):
    name = models.CharField(max_length=45, verbose_name='Name of food')
    author = models.CharField(max_length=35, verbose_name='from author')
    description = models.TextField()
    image = models.ImageField(upload_to='food/%Y/%m')

    class Meta:
        verbose_name_plural = 'Food'

class Gellery(models.Model):
    title = models.CharField(max_length=10)
    safety = models.TextField()
    shah = models.CharField(max_length=50)
    delivery = models.CharField(max_length=125)
    AsiaPark = models.CharField(max_length=100)
    Esen = models.TextField()   
    nav_2019 = models.TextField()
    HoReCa_2018 = models.TextField()
    Tengri_Music_2018 = models.TextField()



# Create your models here.
