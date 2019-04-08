from django.db import models


class Category(models.Model) :
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.category

class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.iso

class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.region

class States(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.states


class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    justification = models.CharField(max_length=1000)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True, blank=True, default=None)
    latitude = models.FloatField(null=True, blank=True, default=None)
    area_hectares = models.FloatField(null=True, blank=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    states = models.ForeignKey(States, on_delete=models.CASCADE, null=True,blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True,blank=True)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self) :
        return self.name, self.description, self.justification, self.year, self.longitude, self.latitude, self.area_hectares, self.category, self.states, self.region, self.iso
