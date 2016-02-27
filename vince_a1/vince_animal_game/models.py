from __future__ import unicode_literals

from django.db import models

# Create your models here.

LANGUAGES_CHOICES = (
    ("ENGLISH", "English"),
    ("SPANISH", "Spanish"),
    ("FRENCH", "French"),
    ("DUTCH", "Dutch"),
    ("DANISH", "Danish"),
)


class Country(models.Model):
    name = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    area = models.IntegerField()
    languages = models.CharField(max_length=8, choices=LANGUAGES_CHOICES)
    population = models.IntegerField()
    landlocked = models.BooleanField()
    gdp = models.IntegerField()



    def __unicode__(self):
        return self.name