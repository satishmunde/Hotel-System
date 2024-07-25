# admin.py
from django.contrib import admin
from .models import Token

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('token_number', 'order', 'is_complated', 'created_at', 'updated_at')
    list_filter = ('is_complated', 'created_at', 'is_complated')
    search_fields = ('token_number', 'is_complated')

