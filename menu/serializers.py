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
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        print('------------------------')
        print(obj.category)
        return obj.category.name  # Returns the name of the category

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Menu item name is required.")
        if len(value) > 200:
            raise serializers.ValidationError("Menu item name must be at most 200 characters long.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value
    
    def validate_availability(self, value):
        if value < 0:
            raise serializers.ValidationError("Availability must be a positive number.")
        return value

    def validate_image(self, value):
        if value:
            if value.size > 5 * 1024 * 1024:
                raise serializers.ValidationError("Image file size must be less than 5MB.")
            if not value.name.endswith(('.jpg', '.jpeg', '.png')):
                raise serializers.ValidationError("Image must be in JPG, JPEG, or PNG format.")
        return value

    def validate(self, data):
        print(data)
        print(data.get('category'))
        category = data.get('category')
        name = data.get('name')

        if MenuItem.objects.filter(name=name, category=category).exists():
            raise serializers.ValidationError("A menu item with this name already exists in the selected category.")
        
        # Inject company from the request user
        data['company'] = self.context['request'].user.company

        return data

    def create(self, validated_data):
        
        print(validated_data)
        # Create a new MenuItem with the validated data
        validated_data['company'] = self.context['request'].user.company
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Update the MenuItem with the validated data
        validated_data['company'] = self.context['request'].user.company
        return super().update(instance, validated_data)

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'category', 'price', 'image', 'availability', 'company']
        read_only_fields = ['is_active', 'company']
