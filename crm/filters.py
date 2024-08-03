# filters.py
import django_filters
from .models import Customer

class CustomerFilter(django_filters.FilterSet):
    
    email = django_filters.CharFilter(lookup_expr='exact')
    class Meta:
        model = Customer
        fields = '__all__'  # Adjust fields as needed
       