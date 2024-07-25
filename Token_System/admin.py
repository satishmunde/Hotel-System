# admin.py
from django.contrib import admin
from .models import Token

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('token_number', 'order',  'created_at', 'updated_at')
    list_filter = ( 'created_at',)
    search_fields = ('token_number',)

