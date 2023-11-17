from django.contrib import admin
from .models import *
my_models = [air_impact, metering_valve]
admin.site.register(my_models)
# Register your models here.
