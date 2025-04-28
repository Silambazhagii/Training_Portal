from django.shortcuts import render, redirect
from .models import Employee, TrainingProgram
from .forms import EmployeeForm, TrainingProgramForm

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'core/employee_list.html', {'employees': employees})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'core/employee_add.html', {'form': form})

def training_list(request):
    trainings = TrainingProgram.objects.all()
    return render(request, 'core/training_list.html', {'trainings': trainings})

def training_add(request):
    if request.method == 'POST':
        form = TrainingProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingProgramForm()
    return render(request, 'core/training_add.html', {'form': form})
