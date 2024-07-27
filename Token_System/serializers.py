from rest_framework import serializers
from .models import TokenOrder, TokenOrderItem

class TokenOrderSerializer(serializers.ModelSerializer):
    def validate_customer_name(self, value):
        # Ensure customer exists
        if not value:
            raise serializers.ValidationError("Customer must be specified.")
        # Assuming Customer model exists and has a valid PK check
        if not value.pk:
            raise serializers.ValidationError("Customer does not exist.")
        return value

    # def validate_status(self, value):
    #     # Ensure status is one of the choices
    #     valid_statuses = dict(TokenOrder.STATUS_CHOICES).keys()
    #     if value not in valid_statuses:
    #         raise serializers.ValidationError(f"Status must be one of the following: {', '.join(valid_statuses)}.")
    #     return value

    def validate_total_amount(self, value):
        # Ensure total_amount is not negative
        if value < 0:
            raise serializers.ValidationError("Total amount cannot be negative.")
        return value

    def validate(self, data):
        # Validate that the total_amount is correctly calculated
        if 'total_amount' in data:
            total_amount = data['total_amount']
            if total_amount < 0:
                raise serializers.ValidationError("Total amount cannot be negative.")
        return data

    class Meta:
        model = TokenOrder
        fields = '__all__'
        read_only_fields = ['is_active', 'token_number', 'total_amount']



class TokenOrderItemSerializer(serializers.ModelSerializer):
    def validate_quantity(self, value):
        # Ensure quantity is a positive integer
        if value <= 0:
            raise serializers.ValidationError("Quantity must be a positive integer.")
        return value

    def validate_extra_tip(self, value):
        # Ensure extra tip is within a reasonable length
        if value and len(value) > 250:
            raise serializers.ValidationError("Extra tip must be at most 250 characters long.")
        return value

    def validate(self, data):
        # Validate that the total is correctly calculated
        item = data.get('item')
        quantity = data.get('quantity')
        if item and quantity:
            expected_total = item.price * quantity
            if 'total' in data and data['total'] != expected_total:
                raise serializers.ValidationError("Total amount does not match the expected value based on quantity and item price.")
        return data

    class Meta:
        model = TokenOrderItem
        fields = '__all__'
