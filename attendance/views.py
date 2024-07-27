from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from datetime import datetime
from .models import Employee, Attendance
from .forms import UserRegistrationForm, AttendanceForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to a login page or any other page
    else:
        form = UserRegistrationForm()
    return render(request, 'attendance/register.html', {'form': form})

def attendance_home(request):
    return render(request, 'attendance/attendance_home.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'attendance/employee_list.html', {'employees': employees})

def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'attendance_records': attendance_records})

def mark_attendance(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.employee = employee
            attendance.date = datetime.now().date()
            attendance.time_in = datetime.now().time()
            attendance.wages = employee.wage_rate * 8 # Assuming 8 hours per day
            attendance.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form, 'employee': employee})

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            aadhar_number = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=aadhar_number, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('employee_list')
    else:
        form = AuthenticationForm()
    return render(request, 'attendance/admin_login.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            aadhar_number = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=aadhar_number, password=password)
            if user is not None and user.is_employee:
                login(request, user)
                return redirect('attendance_list')
    else:
        form = AuthenticationForm()
    return render(request, 'attendance/user_login.html', {'form': form})
