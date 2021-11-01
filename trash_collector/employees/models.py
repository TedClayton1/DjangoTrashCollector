from django.db import models

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories
class Employee_info(models.Model):
    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

def __str__(self):
    return self.name