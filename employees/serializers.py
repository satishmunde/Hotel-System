from datetime import date

from rest_framework import serializers
from .models import Department, Employee, Position, EmployeePosition,Document ,RequiredDocument

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

class EmployeeSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True)  
    def validate(self, data):

        

        if not re.match(r'^[a-zA-Z]+$', data['first_name'] ):
            raise serializers.ValidationError("First Name Contains Only Alfabate")
        
        if not re.match(r'^[a-zA-Z]+$', data['last_name'] ):
            raise serializers.ValidationError("Last Name Contains Only Alfabate")
        
        if not len(data['phone_number']) == 10:
            raise serializers.ValidationError("Please Enter Valid Phone Number")

        if not re.match(r'^[a-zA-Z,. ]+$',data['address']):
            raise serializers.ValidationError("Address Should not Contains Any Special Character")
        
        
        
        
        today = date.today()
        birth_date = data['birth_date']

        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if age < 18:
            raise serializers.ValidationError("Employee must be 18 years or older.")
                
        if not re.match(r'^[a-zA-Z]+$', data['bank_name'] ):
            raise serializers.ValidationError("Bank Name Contains Only Alfabate")
        
        pan_regex = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
        if not re.match(pan_regex, data['pan_number']):
            raise serializers.ValidationError("Invalid PAN number format.")
        
        
        ifsc_regex = r'^[A-Z]{4}0[A-Z0-9]{6}$'
        if not re.match(ifsc_regex, data['bank_ifsc_code']):
            raise serializers.ValidationError("Invalid IFSC code format.")
        

        return data
    
    
    def update(self, instance, validated_data):

        validated_data['member_id']= instance.member_id
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    class Meta:
        model = Employee
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    def validate(self, data):

        if not Position.objects.filter(pk=data['gym'].gym_id).exists():
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
        model = Position
        fields = '__all__'

class EmployeePositionSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not EmployeePosition.objects.filter(pk=data['gym'].gym_id).exists():
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
        model = EmployeePosition
        fields = '__all__'

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

