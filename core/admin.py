from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from core.models import LoginSystem

@admin.register(LoginSystem)
class LoginSystemAdmin(BaseUserAdmin):
    
    add_fieldsets = (
       ('Authentication Creadencial', {
            'fields': ('company','username','access_token','refresh_token', 'email', 'phone_number', 'date_of_birth', 'profile_pictures', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'address', 'aadhar_number', 'pan_number', 'bank_name', 'bank_account_number', 'bank_ifsc_code')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Documents', {
            'fields': ('is_doc_uploaded',)
        }),
    )

    fieldsets = (
        ('Authentication Creadencial', {
            'fields': ('company','emp_id', 'username', 'email', 'phone_number', 'date_of_birth', 'profile_pictures', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'address', 'aadhar_number', 'pan_number', 'bank_name', 'bank_account_number', 'bank_ifsc_code')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Documents', {
            'fields': ('is_doc_uploaded',)
        }),
    )

    list_display = ('username', 'email', 'company','phone_number', 'date_of_birth', 'emp_id', 'is_active', 'first_name', 'last_name')
    search_fields = ('username', 'email','company', 'phone_number', 'date_of_birth', 'first_name', 'last_name', 'address', 'aadhar_number', 'pan_number', 'bank_name', 'bank_account_number', 'bank_ifsc_code')
    ordering = ('company',)
    readonly_fields = ('access_token', 'refresh_token')

    # Add form for creating and updating users
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:  # Editing an existing user
            form.base_fields['password'].widget = forms.HiddenInput()
        return form

    # Override save model to ensure password is handled correctly


from django.contrib import admin
from .models import Company, Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'duration_months', 'price')
    search_fields = ('plan_name',)
    list_filter = ('plan_name',)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'name', 'address', 'contact_number', 'email', 'current_subscription', 'subscription_start_date', 'subscription_end_date', 'is_subscription_active')
    search_fields = ('name', 'address', 'contact_number', 'email')
    list_filter = ('current_subscription', 'is_subscription_active')
    readonly_fields = ('company_id', 'subscription_start_date', 'subscription_end_date')

    def save_model(self, request, obj, form, change):
        if not change:  # If adding a new company
            obj.calculate_subscription_dates()
        super().save_model(request, obj, form, change)

admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Company, CompanyAdmin)
