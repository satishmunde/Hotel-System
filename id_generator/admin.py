# employees/admin.py
from django.contrib import admin
from .models import Identity_Card

@admin.register(Identity_Card)
class IdentityCardAdmin(admin.ModelAdmin):
    list_display = ('employee', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('employee__first_name', 'employee__last_name')
