from rest_framework import serializers
from .models import Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 
        read_only_fields = ['is_active'] 

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested serializer for category

    class Meta:
        model = MenuItem
        fields = '__all__'
        read_only_fields = ['is_active'] 