from django.contrib import admin
from .models import *
my_models = [News]
admin.site.register(my_models)
# Register your models here.
