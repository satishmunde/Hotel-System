# filters.py
import django_filters
from .models import Bill, Payment
class BillFilter(django_filters.FilterSet):
    class Meta:
        model = Bill
        fields = '__all__'  # Adjust fields as needed


class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Payment
        fields = '__all__'  # Adjust fields as needed
