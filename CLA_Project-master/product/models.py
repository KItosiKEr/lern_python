from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'product/%Y/%m', blank=True)

    def __str__(self) -> str:
        return f'name: {self.title}'


# Create your models here.
