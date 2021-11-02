from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls.base import reverse
from .models import employee_info

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')


def create_employee(request):
    logged_in_employee = request.user
    if request.method == "POST":
        employee_name = request.POST.get('name')
        employee_zipcode = request.POST.get('zip_code')
        logged_in_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        context = {
            'logged_in_employee': logged_in_employee
        }
        return render(request, 'employees/create_employee.html', context)   


def edit_employee(request):
    logged_in_user = request.user
    logged_in_employee = employee.objects.get(user=logged_in_user)
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        zip_from_form = request.POST.get('zip_code')
        logged_in_employee.name = name_from_form
        logged_in_employee.zip_code = zip_from_form
        logged_in_employee.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        context = {
            'logged_in_employee': logged_in_employee
        }
        return render(request, 'employee/edit_employee.html', context)   