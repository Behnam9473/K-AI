from django.contrib import admin
from .models import *
# Register your models here.
my_models = [about_us, Testimonials, services, overview]
admin.site.register(my_models)
