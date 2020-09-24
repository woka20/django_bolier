from django.db import models

# Create your models here.

class Hero(models.Model):
    id=models.CharField(max_length=1, primary_key=True)
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    publisher = models.CharField(max_length=400)
    release_date = models.DateField()


    def __str__(self):
        return self.name
