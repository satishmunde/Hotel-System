from datetime import date

from rest_framework import serializers
from .models import Department, Position, EmployeePosition,Document ,RequiredDocument

import re

class DepartmentSerializer(serializers.ModelSerializer):
    def validate(self, data):

        if  Department.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError(" Department Name is Already Exitst")

        return data
    
    def update(self, instance, validated_data):
  
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
    
    # def retrieve(self, instance):

    #     return instance

    # def list(self, queryset):
        
    #     return queryset
    
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['dept_id' ,'is_active'] 

class DocumentSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        if not Document.objects.filter(pk=data['gym'].gym_id).exists():
            raise serializers.ValidationError("Invalid gym ID")

        if data['member_age'] <= 16:
            raise serializers.ValidationError("Age must be a Greater than 16")
        return data
    
    
    def update(self, instance, validated_data):
        validated_data['member_id']= instance.member_id
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ['is_active'] 

class PositionSerializer(serializers.ModelSerializer):
    def validate(self, data):

        if  Position.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError(" Position is Already Exitst")

        return data
    
    def update(self, instance, validated_data):
  
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
    
    class Meta:
        model = Position
        fields = '__all__'
        read_only_fields = ['is_active'] 

class EmployeePositionSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # if not EmployeePosition.objects.filter(pk=data['gym'].gym_id).exists():
        #     raise serializers.ValidationError("Invalid gym ID")

        # if data['member_age'] <= 16:
        #     raise serializers.ValidationError("Age must be a Greater than 16")
        
        return data
    
    
    def update(self, instance, validated_data):

        # validated_data['member_id']= instance.member_id
    
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
    class Meta:
        model = EmployeePosition
        fields = '__all__'
        read_only_fields = ['is_active'] 

class RequireDocumentsSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not RequiredDocument.objects.filter(pk=data['gym'].gym_id).exists():
            raise serializers.ValidationError("Invalid gym ID")

        if data['member_age'] <= 16:
            raise serializers.ValidationError("Age must be a Greater than 16")
        return data
    
    def update(self, instance, validated_data):
        validated_data['member_id']= instance.member_id
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
    class Meta:
        model = RequiredDocument
        fields = '__all__'
        read_only_fields = ['is_active'] 
