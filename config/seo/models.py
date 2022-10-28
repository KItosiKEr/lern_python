from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class Pricing(models.Model):
    list = (
        ('Basic','Basic'),
        ('Standart','Basic'),
        ('Professional','Professional')
    )

    type = models.CharField(max_length=15, choices=list, verbose_name='Pricing plan')
    price = models.IntegerField(verbose_name='price of plan')
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricing Plans'

    def __str__(self):
        return f"plan and price : {self.type, self.price}"

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='title of category')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='title of blog')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    pub_date = models.DateTimeField(auto_now=True, verbose_name='publish date')
    image = models.ImageField(upload_to = 'blog/%Y/%m', verbose_name='image for blog')
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

# Create your models here.
