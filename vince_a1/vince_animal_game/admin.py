from django.contrib import admin

# Register your models here.
from .models import Country
from .models import Question

admin.site.register(Country)
admin.site.register(Question)