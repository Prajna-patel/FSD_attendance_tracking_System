from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15,default='DEFAULT_AADHAAR')
    aadhaar_number = models.CharField(max_length=12, unique=True, default='DEFAULT_AADHAAR')
    address = models.TextField(default='DEFAULT_ADDRESS')

    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True
    )

    def __str__(self):
        return self.username

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    wage_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Wage rate per hour

    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    time_in = models.TimeField(default='09:00:00')  # Default time-in for existing rows
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
    wages = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Wages earned for the day

    def __str__(self):
        return f"{self.employee.user.username} - {self.date} - {self.status}"

# Example of another model (e.g., MyModel)
class MyModel(models.Model):
    my_date_field = models.DateTimeField(default=timezone.now)
    
