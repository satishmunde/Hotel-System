# admin.py
from django.contrib import admin
from .models import TokenOrder, TokenOrderItem


class TokenOrderItemInline(admin.TabularInline):
    model = TokenOrderItem
    extra = 0  # Show no extra forms for adding new items initially

@admin.register(TokenOrder)
class TokenOrderAdmin(admin.ModelAdmin):
    list_display = ('token_number', 'customer_name', 'status', 'total_amount', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    inlines = [TokenOrderItemInline]

    def total_amount(self, obj):
        return obj.total_amount  # Assuming total_amount is a method or property on Order model

    total_amount.short_description = 'Total Amount'

    def get_formset(self, request, obj=None, **kwargs):
        """
        Override get_formset method to handle unsaved Order instance
        """
        formset = super().get_formset(request, obj, **kwargs)
        if obj is None:
            formset.extra = 1  # Allow adding one extra form for new unsaved Order instance
        return formset

