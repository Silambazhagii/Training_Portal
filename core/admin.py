from django.contrib import admin
from .models import Employee, TrainingProgram, Enrollment

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department')
    search_fields = ('name', 'email', 'department')

@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date')
    search_fields = ('title',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'program', 'enrolled_on')
    search_fields = ('employee__name', 'program__title')