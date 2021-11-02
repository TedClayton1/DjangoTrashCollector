from django.db import models


# TODO: Create an Employee model with properties required by the user stories

class employee_info(models.Model):
    name = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__(self):
        return self.name
