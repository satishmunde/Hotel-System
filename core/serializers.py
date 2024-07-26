from datetime import datetime
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer 
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import LoginSystem
from employees.models import Document
from employees.serializers import DocumentSerializer
import re
class LoginSystemSerializer(serializers.ModelSerializer):
    documents = serializers.SerializerMethodField()
    
    def get_documents(self, obj):
        
        documents = Document.objects.filter(employee=obj)  
        return DocumentSerializer(documents, many=True).data

    class Meta:
        model = LoginSystem
        fields = '__all__'
        read_only_fields = ['emp_id'] 
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserCreateSerializer(BaseUserCreateSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = LoginSystem
        fields = [
            'emp_id', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number',
            'profile_pictures', 'address', 'aadhar_number', 'pan_number', 'bank_name',
            'bank_account_number', 'bank_ifsc_code', 'is_doc_uploaded', 'password', 'is_staff',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

        read_only_fields = ['emp_id'] 

    def validate_username(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Username is required.")
        if LoginSystem.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Username already exists (case-insensitive).")
        
        if not value.isalpha():
            raise serializers.ValidationError("username  can contains only String")
        # Additional checks can be added here (e.g., allowed characters)
        return value

    def validate_first_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("First name is required.")
        if len(value) > 100:
            raise serializers.ValidationError("First name cannot exceed 100 characters.")
        if not value.isalpha() :
            raise serializers.ValidationError("First name can have only String ")
        # Additional checks can be added here (e.g., allowed characters)
        return value

    def validate_last_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Last name is required.")
        if len(value) > 100:
            raise serializers.ValidationError("Last name cannot exceed 100 characters.")
        if not value.isalpha() :
            raise serializers.ValidationError("Last name can have only String ")
        # Additional checks can be added here (e.g., allowed characters)
        return value

    def validate_email(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Email is required.")
        if not self.instance or value != self.instance.email:
            if LoginSystem.objects.filter(email=value).exists():
                raise serializers.ValidationError("Email already exists.")
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, value):
            raise serializers.ValidationError("Invalid email format.")
        return value

    # def validate_date_of_birth(self, value):
    #     # Example format: YYYY-MM-DD
    #     if not isinstance(value, str):
    #         raise serializers.ValidationError("Date of birth must be a string in YYYY-MM-DD format.")
    #     try:
    #         datetime.datetime.strptime(value, '%Y-%m-%d')
    #     except ValueError:
    #         raise serializers.ValidationError("Invalid date format. Use YYYY-MM-DD.")
    #     # Additional age checks can be added here
    #     return value

    def validate_phone_number(self, value):
        value = value.strip()
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must be a 10-digit number.")
        # Additional checks can be added here (e.g., country code validation)
        return value

    def validate_address(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Address is required.")
        if len(value) > 255:
            raise serializers.ValidationError("Address cannot exceed 255 characters.")
        # Additional checks can be added here (e.g., allowed characters)
        return value

    def validate_aadhar_number(self, value):
        value = value.strip()
        if not value.isdigit() or len(value) != 12:
            raise serializers.ValidationError("Aadhar number must be a 12-digit number.")
        # Additional checks can be added here (e.g., checksum validation)
        return value

    def validate_pan_number(self, value):
        value = value.strip()
        pan_regex = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
        if not re.match(pan_regex, value):
            raise serializers.ValidationError("Invalid PAN number format.")
        # Additional checks can be added here
        return value

    def validate_bank_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Bank name is required.")
        if len(value) > 100:
            raise serializers.ValidationError("Bank name cannot exceed 100 characters.")
        # Additional checks can be added here (e.g., allowed characters)
        return value

    def validate_bank_account_number(self, value):
        value = value.strip()
        if not value.isdigit() or len(value) < 8 or len(value) > 16:
            raise serializers.ValidationError("Bank account number must be between 8 and 16 digits.")
        # Additional checks can be added here (e.g., checksum validation)
        return value

    def validate_bank_ifsc_code(self, value):
        value = value.strip()
        if len(value) != 11 or not re.match(r"^[A-Z]{4}0[A-Z0-9]{6}$", value):
            raise serializers.ValidationError("Invalid IFSC code format.")
        # Additional checks can be added here
        return value
    
    def create(self, validated_data):
        # Extract password from validated data
        password = validated_data.pop('password', None)
        
        # Create the user instance with the remaining data
        user = super().create(validated_data)
        
        if password:
            user.set_password(password)  # Hash the password
            user.save()
        
        return user


class UserSerializer(BaseUserSerializer):
    documents = serializers.SerializerMethodField()

    class Meta:
        ref_name = "BaseUser"  
        model = LoginSystem


        fields = '__all__'
        read_only_fields = ['emp_id']   
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def get_documents(self, obj):
        
        documents = Document.objects.filter(employee=obj)  
        return DocumentSerializer(documents, many=True).data
