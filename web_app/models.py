from django.db import models
from django.utils import timezone


class Person(models.Model):
    GENDER = [
        ('FE', 'Female'),
        ('MA', 'Male'),
    ]
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40, blank=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default='MA',
    )
    age = models.CharField(
        max_length=2,
        blank=True
    )

    def __str__(self):
        return self.name


class Coordinate(models.Model):
    person = models.ForeignKey('Person', related_name='coordinates', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField(max_length=30, null=True)
    longitude = models.FloatField(max_length=30, null=True)
