from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Attendance

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'aadhaar_number', 'address', 'password1', 'password2', 'is_admin', 'is_employee']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'status']
