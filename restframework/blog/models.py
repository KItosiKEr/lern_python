from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=25)
    desc = models.TextField()
    
# Create your models here.
