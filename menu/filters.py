# filters.py
import django_filters
from .models import Category, MenuItem

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemFilter(django_filters.FilterSet):
    class Meta:
        model = MenuItem
        fields = ['name', 'description',]  # include 'image' if needed

  