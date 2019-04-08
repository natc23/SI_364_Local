from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Iso(models.Model):
    iso = models.CharField(max_length=128)

    def __str__(self) :
        return self.Iso

class Region(models.Model):
    region = models.CharField(max_length=128)

    def __str__(self) :
        return self.region


class Site(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    justification = models.CharField(max_length=1000)
    year = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    area_hectares = models.IntegerField(null=True)
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name, self.description, self.justification, self.year, self.longitude, self.latitude, self.area_hectares, self.states, self.region, self.iso

class States(models.Model):

    states = models.CharField(max_length=128)

    def __str__(self) :
        return self.states
