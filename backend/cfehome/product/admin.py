import imp
from django.contrib import admin
from .models import Product, Manufacturer

admin.site.register(Product)
admin.site.register(Manufacturer)

# Register your models here.
