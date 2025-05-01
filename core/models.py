from django.db import models

class TrainingProgram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration_days = models.IntegerField()

    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    def __str__(self):
        return f"{self.employee} enrolled in {self.training_program}"
