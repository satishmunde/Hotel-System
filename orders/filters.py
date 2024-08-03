# filters.py
import django_filters
from .models import Order, OrderItem

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'  # Add specific fields if you want to restrict the filter fields

class OrderItemFilter(django_filters.FilterSet):
    class Meta:
        model = OrderItem
        fields = '__all__'  # Add specific fields if you want to restrict the filter fields
