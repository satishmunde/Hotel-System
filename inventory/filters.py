# filters.py
import django_filters
from .models import InventoryItem, Supplier, PurchaseOrder, PurchaseOrderItem, Expense

class InventoryItemFilter(django_filters.FilterSet):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class SupplierFilter(django_filters.FilterSet):
    class Meta:
        model = Supplier
        fields = '__all__'

class PurchaseOrderFilter(django_filters.FilterSet):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderItemFilter(django_filters.FilterSet):
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'

class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = '__all__'
