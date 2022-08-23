from django.contrib import admin
from .models import Hotel, Reservation

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Hotel)