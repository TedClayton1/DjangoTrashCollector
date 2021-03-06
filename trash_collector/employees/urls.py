from django.urls import path
from . import views

# TODO: Determine what distinct pages are required for the user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('edit_employee/', views.edit_employee, name="edit_employee"),
    path('confirm/<int:customer_id>', views.confirm, name="confirm")
]