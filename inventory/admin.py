from django.contrib import admin
from .models import InventoryItem, Supplier, PurchaseOrder, PurchaseOrderItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'reorder_level')
    search_fields = ('name',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','company', 'email','phone','address')
    search_fields = ('name','company',)





from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date', 'category')
    search_fields = ('description', 'category')
    list_filter = ('date', 'category')



class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem
    extra = 0  # Show no extra forms for adding new items initially
    
from django.contrib import admin
from .models import PurchaseOrder, PurchaseOrderItem

class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem
    extra = 1  # Number of extra forms to display
    fields = ('inventory_item', 'quantity', 'total')

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'display_total_amount', 'supplier', 'is_completed')
    search_fields = ('supplier__name',)
    list_filter = ('order_date', 'is_completed')
    inlines = [PurchaseOrderItemInline]

    def display_total_amount(self, obj):
        return obj.total_amount  # This should be a field in the PurchaseOrder model

    display_total_amount.short_description = 'Total Amount'

    def get_formset(self, request, obj=None, **kwargs):
        """
        Override get_formset method to handle unsaved Order instance
        """
        formset = super().get_formset(request, obj, **kwargs)
        if obj is None:
            formset.extra = 1  # Allow adding one extra form for new unsaved Order instance
        return formset

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.calculate_total_amount()
