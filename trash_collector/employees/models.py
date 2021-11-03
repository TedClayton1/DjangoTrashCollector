from django.db import models


# TODO: Create an Employee model with properties required by the user stories

class Employee(models.Model):
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default=None)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name