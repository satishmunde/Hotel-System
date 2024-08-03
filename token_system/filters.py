# filters.py
import django_filters
from .models import TokenOrder, TokenOrderItem

class TokenOrderFilter(django_filters.FilterSet):
    class Meta:
        model = TokenOrder
        fields = '__all__'  # Adjust fields if needed

class TokenOrderItemFilter(django_filters.FilterSet):
    class Meta:
        model = TokenOrderItem
        fields = '__all__'  # Adjust fields if needed
