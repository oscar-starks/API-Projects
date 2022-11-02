from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Hotel(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length= 300)
    number_of_reservations = models.IntegerField()
    website = models.URLField()
    date_founded = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.location

    
class Reservation(models.Model):
    res_for = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "res_for")
    duration_of_stay = models.IntegerField()
    signing_in_on = models.DateField()
    signing_out_on = models.DateField()
    email = models.EmailField()
    price = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5000000)])
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, related_name="hotel")
    user_image =  models.ImageField(blank = True, null = True, upload_to = "reservation/")
    
    def __str__(self):
        return self.email