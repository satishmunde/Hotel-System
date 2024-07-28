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


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'total_amount', 'supplier', 'is_completed')
    search_fields = ('supplier__name',)
    list_filter = ('order_date', 'is_completed')


@admin.register(PurchaseOrderItem)
class PurchaseOrderItemAdmin(admin.ModelAdmin):
    list_display = ('purchase_order', 'inventory_item', 'quantity', 'price')
    search_fields = ('purchase_order__id', 'inventory_item__name')


from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date', 'category')
    search_fields = ('description', 'category')
    list_filter = ('date', 'category')
