from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=50)
    massage = models.TextField()
    publish_date = models.DateField()   

# Create your models here.
