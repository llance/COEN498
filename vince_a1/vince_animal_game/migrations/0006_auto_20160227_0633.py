# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vince_animal_game', '0005_question_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='answer',
            new_name='answered',
        ),
        migrations.AddField(
            model_name='question',
            name='asked',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
