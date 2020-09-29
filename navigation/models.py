from django.db import models
from datetime import datetime


class Vehicle(models.Model):
    plate = models.CharField(max_length=12)

    def __str__(self):
        return self.plate


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    nav_record_time = models.DateTimeField(default=datetime.now)
    latitude = models.FloatField()
    longitude = models.FloatField()
