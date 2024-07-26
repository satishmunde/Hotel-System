from rest_framework import serializers
from .models import  TokenOrder, TokenOrderItem


class TokenOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenOrder
        fields = '__all__'
        read_only_fields = ['is_complated'] 
        
class TokenOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenOrderItem
        fields = '__all__'
        # read_only_fields = ['is_complated'] 