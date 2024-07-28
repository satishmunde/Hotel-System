from django.contrib import admin
from .models import Bill, Payment

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('bill_id', 'order', 'customer_id', 'subtotal', 'total_amount')
    search_fields = ('bill_id', 'order__order_id')  # Adjust based on the actual field names
    readonly_fields = ('bill_id',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'order',  'bill', 'payment_date', 'payment_method', 'amount_paid')
    search_fields = ('payment_id', 'order__order_id', 'bill__bill_id')
    list_filter = ('payment_method', 'payment_date')
    readonly_fields = ('payment_id',)
