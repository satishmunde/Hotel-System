from rest_framework import serializers
from .models import Bill, Payment

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['bill_id', 'order', 'customer_id', 'subtotal', 'total_amount']

    def validate_subtotal(self, value):
        if value < 0:
            raise serializers.ValidationError("Subtotal cannot be negative.")
        return value

    def validate_total_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Total amount cannot be negative.")
        return value

    def validate(self, data):
        if data['subtotal'] > data['total_amount']:
            raise serializers.ValidationError("Total amount must be greater than or equal to subtotal.")
        return data




class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'order', 'bill', 'payment_date', 'payment_method', 'amount_paid']

    def validate_amount_paid(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount paid must be greater than zero.")
        return value

    def validate_payment_method(self, value):
        if value not in dict(Payment.PAYMENT_METHOD_CHOICES).keys():
            raise serializers.ValidationError("Invalid payment method.")
        return value
