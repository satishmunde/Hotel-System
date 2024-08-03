import django_filters
from .models import Identity_Card

class Identity_CardFilter(django_filters.FilterSet):
    class Meta:
        model = Identity_Card
        fields = ['employee','created_at','is_active']