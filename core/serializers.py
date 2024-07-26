from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer 
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import LoginSystem



from rest_framework import serializers
from employees.models import Document
from employees.serializers import DocumentSerializer

class LoginSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginSystem
        fields = [
            'emp_id','username', 'first_name', 'last_name', 'email', 'date_of_birth',
            'phone_number',  'profile_pictures', 'address',
            'aadhar_number', 'pan_number', 'bank_name', 'bank_account_number',
            'bank_ifsc_code', 'is_doc_uploaded'
        ]


class UserCreateSerializer(BaseUserCreateSerializer):
    password = serializers.CharField(write_only=True)  # Handle password as write-only

    class Meta:
        model = LoginSystem
        fields = [
           'emp_id', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number',
            'profile_pictures', 'address', 'aadhar_number', 'pan_number', 'bank_name',
            'bank_account_number', 'bank_ifsc_code', 'is_doc_uploaded', 'password' , 'is_staff',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

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
        fields =[
           'emp_id', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number',
            'profile_pictures', 'address', 'aadhar_number', 'pan_number', 'bank_name',
            'bank_account_number', 'bank_ifsc_code', 'is_doc_uploaded', 'password' , 'is_staff','documents',
        ]

    def get_documents(self, obj):
        
        documents = Document.objects.filter(user=obj)  
        return DocumentSerializer(documents, many=True).data
