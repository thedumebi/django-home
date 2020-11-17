from django.db import models

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=128, null=True)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name = models.CharField(max_length=128, null=True)
    
    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=128, null=True)
    
    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128, null=True)
    
    def __str__(self) :
        return self.name


#name,description,justification,year,longitude,latitude,area_hectares,category,states,region,iso

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    justification = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    area_hectares = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)


    def __str__(self) :
        return self.name