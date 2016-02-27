# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vince_animal_game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.CharField(choices=[('NORTH AMERICA', 'North America'), ('CENTRAL AMERICA', 'Central America'), ('CARIBBEAN', 'Caribbean'), ('SOUTH AMERICA', 'South America')], max_length=120),
        ),
    ]
