from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('trainings/', views.training_list, name='training_list'),
    path('trainings/add/', views.training_add, name='training_add'),
]
