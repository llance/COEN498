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

REGION_CHOICES = (
    ("NORTH AMERICA", "North America"),
    ("CENTRAL AMERICA", "Central America"),
    ("CARIBBEAN", "Caribbean"),
    ("SOUTH AMERICA", "South America"),
)

CATEGORY_CHOICES = (
    ("REGION", "Region"),
    ("LANGUAGE", "Language"),
    ("POPULATION", "Population"),
    ("AREA", "Area"),
    ("LANDLOCKED", "Landlocked"),
    ("GDP", "GDP"),
)

class Country(models.Model):
    name = models.CharField(max_length=120)
    region = models.CharField(max_length=120, choices=REGION_CHOICES)
    area = models.IntegerField()
    languages = models.CharField(max_length=8, choices=LANGUAGES_CHOICES)
    population = models.IntegerField()
    landlocked = models.BooleanField()
    gdp = models.IntegerField()



    def __unicode__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length=120)
    category = models.CharField(max_length=120, choices=CATEGORY_CHOICES)
    query_field = models.CharField(max_length=120)
    asked = models.BooleanField()

    def __unicode__(self):
        return self.question