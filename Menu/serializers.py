from rest_framework import serializers
from .models import Category,MenuItem

class CategorySerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        # Clean the data
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Category name is required.")
        if len(value) > 100:
            raise serializers.ValidationError("Category name must be at most 100 characters long.")
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("A category with this name already exists.")
        return value

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['is_active']



class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  # For writable category field

    def validate_name(self, value):
        # Clean the data
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Menu item name is required.")
        if len(value) > 200:
            raise serializers.ValidationError("Menu item name must be at most 200 characters long.")
        if MenuItem.objects.filter(name=value).exists():
            raise serializers.ValidationError("A menu item with this name already exists.")
        return value

    def validate_price(self, value):
        # Validate that price is a positive number
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    def validate_image(self, value):
        # Validate the image field if necessary
        if value:
            # Check image file size (example: limit to 5MB)
            if value.size > 5 * 1024 * 1024:
                raise serializers.ValidationError("Image file size must be less than 5MB.")
            # Check file extension
            if not value.name.endswith(('.jpg', '.jpeg', '.png')):
                raise serializers.ValidationError("Image must be in JPG, JPEG, or PNG format.")
        return value

    def validate(self, data):
        """
        Check if a MenuItem with the same name and category already exists.
        """
        category = data.get('category')
        name = data.get('name')

        if MenuItem.objects.filter(name=name, category=category).exists():
            raise serializers.ValidationError("A menu item with this name already exists in the selected category.")

        return data

    class Meta:
        model = MenuItem
        fields = '__all__'
        read_only_fields = ['is_active']
