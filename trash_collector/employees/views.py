from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from trash_collector.customers.views import one_time_pickup
from .models import Employee
from datetime import datetime

# Create your views here.
# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.

@login_required
def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    logged_in_user = request.user
    try:
        logged_in_employee = Employee.objects.get(user=logged_in_user)
        
        todays_date = datetime.today()
        weekday_name = todays_date.strftime('%A')

        customers = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
        today_customers = customers.filter(weekly_pickup=weekday_name) | customers.filter(one_time_pickup=weekday_name)
        active_pickups = today_customers.exclude(suspend_start__lt=todays_date, suspend_end__gt=todays_date)
        active_pickups = active_pickups.exclude(date_of_last_pickup = todays_date)
        extra_pickup = customers.filter(one_time_pickup=weekday_name)


        context = {
            'logged_in_employee': logged_in_employee,
            'todays_date': todays_date,
            'active_pickups': active_pickups,
            'extra_pickup': extra_pickup
        }
        return render(request, 'employees/index.html', context)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))


@login_required
def create(request):
    logged_in_user = request.user
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        zip_from_form = request.POST.get('zip_code')
        new_employee = Employee(name=name_from_form, user=logged_in_user, address=address_from_form, zip_code=zip_from_form)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


@login_required
def edit_employee(request):
    logged_in_user = request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        zip_from_form = request.POST.get('zip_code')
        logged_in_employee.name = name_from_form
        logged_in_employee.address = address_from_form
        logged_in_employee.zip_code = zip_from_form
        logged_in_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        context = {
            'logged_in_employee': logged_in_employee
        }
        return render(request, 'employees/edit_employee.html', context)


@login_required
def filter_customers(request):
    Customer = apps.get.model('customers.Customer')
    customers = Customer.objects.filter(weekly_pickup='')
    context = {
        'customers':customers
    }
    return render(request, 'employees/index.html', context)


@login_required
def confirm(request, customer_id):
    Customer = apps.get_model('customers.Customer')
    customer_from_db = Customer.objects.get(pk=customer_id)
    today = date.today()
    customer_from_db.date_of_last_pickup = today
    customer_from_db.balance += 20
    customer_from_db.save()
    return HttpResponseRedirect(reverse('employees:index'))