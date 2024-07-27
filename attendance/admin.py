from django.contrib import admin
from .models import User, Employee, Attendance

# Custom admin class for User
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_employee')
    search_fields = ('username', 'email')

# Custom admin class for Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'department')
    search_fields = ('user__username', 'department')

# Custom admin class for Attendance
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    list_filter = ('date', 'status')
    search_fields = ('employee__user__username', 'date')

# Register the models with the admin site using the custom admin classes
admin.site.register(User, UserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
