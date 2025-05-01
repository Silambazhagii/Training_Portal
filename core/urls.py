from django.urls import path
from . import views

urlpatterns = [
    # path('employees/add/', views.employee_add, name=''),
    # path('enrollments/', views.filtered_enrollments, name='filtered-enrollments'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'),

]