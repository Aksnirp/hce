from django.db import models
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone= models.IntegerField(max_length=100,default=0)
    email=models.CharField(max_length=100,default=0)
    address=models.CharField(max_length=100,default=0)

def __str__(self):
        return self.name