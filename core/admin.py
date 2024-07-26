from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from core.models import LoginSystem

@admin.register(LoginSystem)
class LoginSystemAdmin(BaseUserAdmin):
    # Fields to use when adding a new LoginSystem user
    add_fieldsets = (
       (None, {
            'fields': ('username', 'email', 'phone_number', 'date_of_birth', 'profile_pictures', 'password1', 'password2')
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

    # Fields to use when editing an existing LoginSystem user
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'phone_number', 'date_of_birth', 'profile_pictures', 'password')
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

    list_display = ('username', 'email', 'phone_number', 'date_of_birth', 'profile_pictures', 'is_active', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'phone_number', 'date_of_birth', 'first_name', 'last_name', 'address', 'aadhar_number', 'pan_number', 'bank_name', 'bank_account_number', 'bank_ifsc_code')
    ordering = ('username',)

    # Add form for creating and updating users
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:  # Editing an existing user
            form.base_fields['password'].widget = forms.HiddenInput()
        return form

    # Override save model to ensure password is handled correctly
