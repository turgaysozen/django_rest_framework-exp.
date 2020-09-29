from django.db import models


class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    collection_frequency = models.IntegerField(blank=True, null=True)
    last_collection = models.DateField(blank=True, null=True)


class Operation(models.Model):
    bin = models.ForeignKey(Bin, models.CASCADE)
    name = models.CharField(max_length=100)
    operation_date = models.DateField()
