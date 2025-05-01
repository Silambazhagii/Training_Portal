from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'core/employee_list.html', {'employees': employees})
