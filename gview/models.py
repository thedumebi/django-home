from django.db import models

# Create your models here.

from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Horse(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

