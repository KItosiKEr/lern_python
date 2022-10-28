from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField() 
    quantity = models.IntegerField()
    categoty = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=50)



# Create your models here.
