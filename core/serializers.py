from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer 
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import LoginSystem
from employees.models import Document
from employees.serializers import DocumentSerializer

class LoginSystemSerializer(serializers.ModelSerializer):
    documents = serializers.SerializerMethodField()
    
    def get_documents(self, obj):
        
        documents = Document.objects.filter(employee=obj)  
        return DocumentSerializer(documents, many=True).data

    class Meta:
        model = LoginSystem
        # fields = [
        #     'emp_id','username', 'first_name', 'last_name', 'email', 'date_of_birth',
        #     'phone_number',  'profile_pictures', 'address',
        #     'aadhar_number', 'pan_number', 'bank_name', 'bank_account_number',
        #     'bank_ifsc_code', 'is_doc_uploaded'
          
        # ]
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

    def validate(self, data):
        # Check for existing user with the same username
        if LoginSystem.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError("Username already exists.")

        # Check for valid email
        email = data.get('email')
        if email and LoginSystem.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists.")

        # Validate phone number (example: ensure it's 10 digits)
        phone_number = data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise serializers.ValidationError("Phone number should contain only digits.")
        if phone_number and len(phone_number) != 10:
            raise serializers.ValidationError("Phone number should be 10 digits long.")

        # Validate Aadhar number (example: ensure it's 12 digits)
        aadhar_number = data.get('aadhar_number')
        if aadhar_number and not aadhar_number.isdigit():
            raise serializers.ValidationError("Aadhar number should contain only digits.")
        if aadhar_number and len(aadhar_number) != 12:
            raise serializers.ValidationError("Aadhar number should be 12 digits long.")

        # Validate PAN number (example: ensure it's 10 characters long and uppercase)
        pan_number = data.get('pan_number')
        if pan_number and (len(pan_number) != 10 or not pan_number.isupper()):
            raise serializers.ValidationError("PAN number should be 10 uppercase characters.")

        # Validate bank account number (example: ensure it's numeric)
        bank_account_number = data.get('bank_account_number')
        if bank_account_number and not bank_account_number.isdigit():
            raise serializers.ValidationError("Bank account number should contain only digits.")

        # Validate IFSC code (example: ensure it's 11 characters and uppercase)
        bank_ifsc_code = data.get('bank_ifsc_code')
        if bank_ifsc_code and (len(bank_ifsc_code) != 11 or not bank_ifsc_code.isupper()):
            raise serializers.ValidationError("IFSC code should be 11 uppercase characters.")

        # Validate date of birth (example: ensure it's a valid date)
        # date_of_birth = data.get('date_of_birth')
        # if date_of_birth:
        #     from datetime import datetime
        #     try:
        #         datetime.strptime(date_of_birth, '%Y-%m-%d')    
        #     except ValueError:
        #         raise serializers.ValidationError("Date of birth must be in YYYY-MM-DD format.")

        return data

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
        # fields =[
        #    'emp_id', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number',
        #     'profile_pictures', 'address', 'aadhar_number', 'pan_number', 'bank_name',
        #     'bank_account_number', 'bank_ifsc_code', 'is_doc_uploaded', 'password' , 'is_staff','documents',
        # ]
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

        fields = '__all__'
        read_only_fields = ['emp_id']   
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def get_documents(self, obj):
        
        documents = Document.objects.filter(employee=obj)  
        return DocumentSerializer(documents, many=True).data
