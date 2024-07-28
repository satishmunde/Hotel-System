# admin.py
from django.contrib import admin
from .models import Department, Position, EmployeePosition,Document

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
    
    
@admin.register(Document)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('employee','document_type','is_active')

from django.contrib import admin
from .models import EmployeePayment

class EmployeePaymentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'payment_date', 'amount', 'payment_method', 'description')
    search_fields = ('employee__username', 'payment_method', 'description')
    list_filter = ('payment_date', 'payment_method')
    ordering = ('-payment_date',)

admin.site.register(EmployeePayment, EmployeePaymentAdmin)
