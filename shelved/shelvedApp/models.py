from django.db import models
from mongoengine import *
from djangotoolbox.fields import ListField


class Post(models.Model):
    title = models.TextField()
    text = models.TextField()
    tags = ListField()
    comments = ListField()