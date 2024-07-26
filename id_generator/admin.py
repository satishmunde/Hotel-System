# employees/admin.py
from django.contrib import admin
from django.forms import ValidationError
from .models import Identity_Card
from django.contrib.auth import get_user_model
from django.contrib import admin
User = get_user_model()
from .models import Identity_Card
from django.contrib import admin
from .models import Identity_Card
from django.contrib.auth import get_user_model

User = get_user_model()

class IdentityCardAdmin(admin.ModelAdmin):
    fields = ['employee', 'card_pdf', 'is_active']
    readonly_fields = ['created_at']
    list_display = ['employee', 'card_pdf', 'created_at', 'is_active']

    def save_model(self, request, obj, form, change):
        # Ensure the employee exists
        if obj.employee and not User.objects.filter(id=obj.employee.id).exists():
            raise ValidationError("Invalid employee ID.")
        super().save_model(request, obj, form, change)

admin.site.register(Identity_Card, IdentityCardAdmin)
