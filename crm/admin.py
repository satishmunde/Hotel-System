from django.contrib import admin
from .models import Customer
from Orders.models import Order  # Adjust import as per your app structure

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'created_at', 'total_orders')
    list_filter = ('created_at', 'phone', 'name', 'email')

    def total_orders(self, obj):
        return obj.order_set.count()

    total_orders.short_description = 'Total Orders'

admin.site.register(Customer, CustomerAdmin)
