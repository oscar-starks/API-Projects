from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    founder = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    price = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.CASCADE, default = 1, related_name="manufacturer")
    
    
    def __str__(self):
        return self.name
    
