from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['is_active']  # Prevent modification of this field

    def validate_name(self, value):
        # Validate 'name' field regardless of the request method
        if not value:
            raise serializers.ValidationError("Name field cannot be empty.")
        return value

    def validate_email(self, value):
        # Validate 'email' field regardless of the request method
        if Customer.objects.filter(email=value).exclude(phone=self.instance.phone if self.instance else None).exists():
            raise serializers.ValidationError("A customer with this email already exists.")
        return value

    def validate_phone(self, value):
        # Validate 'phone' field regardless of the request method
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must be a 10-digit number.")
        return value