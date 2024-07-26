# admin.py
from django.contrib import admin
from .models import Department, Position, EmployeePosition

# Register your models here

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(EmployeePosition)
class EmployeePositionAdmin(admin.ModelAdmin):
    list_display = ('employee', 'department', 'position', 'start_date', 'end_date')
    list_filter = ('department', 'position', 'start_date', 'end_date')
    search_fields = ('employee__first_name', 'employee__last_name', 'position__name')
