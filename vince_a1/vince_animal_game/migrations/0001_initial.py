# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('region', models.CharField(max_length=120)),
                ('area', models.IntegerField()),
                ('languages', models.CharField(choices=[('ENGLISH', 'English'), ('SPANISH', 'Spanish'), ('FRENCH', 'French'), ('DUTCH', 'Dutch'), ('DANISH', 'Danish')], max_length=8)),
                ('population', models.IntegerField()),
                ('landlocked', models.BooleanField()),
                ('gdp', models.IntegerField()),
            ],
        ),
    ]