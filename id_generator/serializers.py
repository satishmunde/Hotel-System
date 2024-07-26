

from rest_framework import serializers
from .models import Identity_Card
from django.contrib.auth import get_user_model

User = get_user_model()

class IDCardSerializer(serializers.ModelSerializer):
    # def validate(self, data):
    #     # Check if employee exists
    #     employee = data.get('employee')
    #     if employee and not User.objects.filter(id=employee.id).exists():
    #         raise serializers.ValidationError("Invalid employee ID.")

    #     return data

    class Meta:
        model = Identity_Card
        fields = '__all__'
        read_only_fields = ['created_at', 'is_active']
