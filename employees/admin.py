# admin.py
from django.contrib import admin
from .models import Department, Employee, Position, EmployeePosition

# Register your models here

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'is_active')
    list_filter = ('is_active', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(EmployeePosition)
class EmployeePositionAdmin(admin.ModelAdmin):
    list_display = ('employee', 'department', 'position', 'start_date', 'end_date')
    list_filter = ('department', 'position', 'start_date', 'end_date')
    search_fields = ('employee__first_name', 'employee__last_name', 'position__title')
