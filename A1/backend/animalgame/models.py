# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Data(models.Model):
    object_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'


class Objects(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    name = models.TextField(blank=True, null=True)
    created = models.DateField(blank=True, null=True)
    times_played = models.IntegerField(blank=True, null=True)
    last_played = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objects'


class Questions(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    text = models.TextField(blank=True, null=True)
    created = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'
