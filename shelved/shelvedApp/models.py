from django.db import models

class Post(models.Model):
    title = models.TextField()
    text = models.TextField()
