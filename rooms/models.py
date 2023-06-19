from django.db import models
from .enum import RoomType


class Resident(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Availability(models.Model):
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.start_time} || {self.end_time}"

    class Meta:
        verbose_name = 'Availability'
        verbose_name_plural = 'Availabilities'


class Room(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=RoomType.choices())
    capacity = models.IntegerField()
    resident = models.ForeignKey(Resident, blank=True, null=True, on_delete=models.SET_NULL)
    availability = models.ManyToManyField(Availability)

    def __str__(self):
        return self.name




