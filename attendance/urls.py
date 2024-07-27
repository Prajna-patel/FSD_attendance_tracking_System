from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_home, name='attendance_home'),
    path('employees/', views.employee_list, name='employee_list'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('mark_attendance/<int:employee_id>/', views.mark_attendance, name='mark_attendance'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
]
