# serializers.py
from rest_framework import serializers
from .models import Identity_Card

class IDCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identity_Card
        fields = '__all__'
