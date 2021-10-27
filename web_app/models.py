from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Person(models.Model):

    class Gender(models.TextChoices):
        FEMALE = 'FE', _('Female')
        MALE = 'MA', _('Male')

    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40, blank=True)
    gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
        default=Gender.FEMALE,
    )
    age = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.name

    def get_gender(self):
        return self.gender


class Coordinate(models.Model):
    person = models.ForeignKey('Person', related_name='coordinates', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField(max_length=30, null=True)
    longitude = models.FloatField(max_length=30, null=True)
