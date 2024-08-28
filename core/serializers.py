from datetime import datetime, timezone
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer 
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import LoginSystem,Company
from employees.models import Document,EmployeePosition
from employees.serializers import DocumentSerializer,EmployeePositionSerializer
import re
from django.contrib.auth.models import Group  # Example import
from .models import Company, Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
    
    def validate_duration_months(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be a positive integer.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

class CompanySerializer(serializers.ModelSerializer):
    current_subscription = SubscriptionSerializer()
    class Meta:
        model = Company
        fields = '__all__'
    
    def validate_email(self, value):
        if Company.objects.exclude(pk=self.instance.pk).filter(email=value).exists():
            raise serializers.ValidationError("A company with this email already exists.")
        return value

    def validate_contact_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number must contain only digits.")
        if len(value) < 10:
            raise serializers.ValidationError("Contact number must be at least 10 digits long.")
        return value

    def validate(self, data):
        # Example validation to check if subscription is active
        if data.get('subscription_end_date') and data.get('subscription_end_date') <= timezone.now().date():
            data['is_subscription_active'] = False
        return data



class LoginSystemSerializer(BaseUserSerializer,serializers.ModelSerializer):
    documents = serializers.SerializerMethodField()
    employee_position = serializers.SerializerMethodField()
    company = serializers.SerializerMethodField()

    
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True, required=False)  # Example

    def __init__(self, *args, **kwargs):
        request_method = kwargs['context']['request'].method if 'request' in kwargs['context'] else None

        # Define fields to be included for POST, GET, and PUT requests
        fields_for_post = [field.name for field in LoginSystem._meta.fields if field.name not in [
            'emp_id', 'last_updated', 'created_at', 'password', 'access_token', 'refresh_token']]
        fields_for_get = [field.name for field in LoginSystem._meta.fields if field.name not in [
            'password']] + ['documents','employee_position',]
        fields_for_put = [field.name for field in LoginSystem._meta.fields if field.name not in [
            'last_updated', 'created_at', 'password', 'last_login', 'is_superuser', 'is_staff', 'date_joined', 
            'access_token', 'refresh_token', 'is_active', 'is_doc_uploaded']]

        if request_method == 'POST':
            fields_to_keep = fields_for_post
        elif request_method == 'GET':
            fields_to_keep = fields_for_get
        elif request_method == 'PUT':
            fields_to_keep = fields_for_put
        else:
            fields_to_keep = None
            

        if fields_to_keep is not None:
            self.fields = {field_name: self.fields[field_name] for field_name in fields_to_keep if field_name in self.fields}
            
            # Make `password` field optional for PUT requests
            if request_method == 'PUT':
                for field_name in fields_to_keep:
                    if field_name in self.fields:
                        self.fields[field_name].required = False
            


        super().__init__(*args, **kwargs)

    def get_documents(self, obj):
        documents = Document.objects.filter(employee=obj)
        return DocumentSerializer(documents, many=True).data
    
    def get_company(self, obj):
        company = Company.objects.filter(company_id=obj.company.company_id)
        return CompanySerializer(company, many=True).data
    

    def get_employee_position(self, obj):
        employee_position = EmployeePosition.objects.filter(employee=obj)
        return EmployeePositionSerializer(employee_position, many=True).data

    def update(self, instance, validated_data):
        # Handle many-to-many fields separately
        groups = validated_data.pop('groups', None)
        password = validated_data.pop('password', None)  # Extract password if provided
        
        # Update the instance with other validated data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password is not None:  # Only update password if it's provided
            instance.set_password(password)  # Handle password update safely

        if groups is not None:
            instance.groups.set(groups)  # Use `set()` to handle many-to-many relationships

        instance.save()
        return instance



    class Meta:
        model = LoginSystem
        fields = '__all__'
        read_only_fields = ['emp_id']  # Ensure emp_id is read-only




    def validate_username(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Username is required.")
        if LoginSystem.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Username already exists (case-insensitive).")
        if not re.match(r'^[\w\s,.]+$', value):  # Allow letters, digits, spaces, commas, periods
            raise serializers.ValidationError("Username can contain only letters, digits, spaces, commas, and periods.")
        return value

    def validate_first_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("First name is required.")
        if len(value) > 100:
            raise serializers.ValidationError("First name cannot exceed 100 characters.")
        if not re.match(r'^[a-zA-Z\s,.]+$', value):  # Allow letters, spaces, commas, periods
            raise serializers.ValidationError("First name can contain only letters, spaces, commas, and periods.")
        return value

    def validate_last_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Last name is required.")
        if len(value) > 100:
            raise serializers.ValidationError("Last name cannot exceed 100 characters.")
        if not re.match(r'^[a-zA-Z\s,.]+$', value):  # Allow letters, spaces, commas, periods
            raise serializers.ValidationError("Last name can contain only letters, spaces, commas, and periods.")
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

    def validate_phone_number(self, value):
        value = value.strip()
        if not re.match(r'^\d{10}$', value):  # Ensure it is exactly 10 digits
            raise serializers.ValidationError("Phone number must be a 10-digit number.")
        return value

    def validate_address(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Address is required.")
        if len(value) > 255:
            raise serializers.ValidationError("Address cannot exceed 255 characters.")
        if not re.match(r'^[\w\s,.]+$', value):  # Allow letters, digits, spaces, commas, periods
            raise serializers.ValidationError("Address can contain only letters, digits, spaces, commas, and periods.")
        return value

    def validate_aadhar_number(self, value):
        value = value.strip()
        if not re.match(r'^\d{12}$', value):  # Ensure it is exactly 12 digits
            raise serializers.ValidationError("Aadhar number must be a 12-digit number.")
        return value

    def validate_pan_number(self, value):
        value = value.strip()
        pan_regex = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
        if not re.match(pan_regex, value):
            raise serializers.ValidationError("Invalid PAN number format.")
        return value

    def validate_bank_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Bank name is required.")
        if len(value) > 100:
            raise serializers.ValidationError("Bank name cannot exceed 100 characters.")
        if not re.match(r'^[\w\s,.]+$', value):  # Allow letters, spaces, commas, periods
            raise serializers.ValidationError("Bank name can contain only letters, spaces, commas, and periods.")
        return value

    def validate_bank_account_number(self, value):
        value = value.strip()
        if not re.match(r'^\d{8,16}$', value):  # Ensure it is between 8 and 16 digits
            raise serializers.ValidationError("Bank account number must be between 8 and 16 digits.")
        return value

    def validate_bank_ifsc_code(self, value):
        value = value.strip()
        if not re.match(r'^[A-Z]{4}0[A-Z0-9]{6}$', value) or len(value) != 11:
            raise serializers.ValidationError("Invalid IFSC code format.")
        return value

    def validate_date_of_birth(self, value):
        import datetime

        today = datetime.date.today()
        dob = value  # Ensure `value` is a datetime.date object
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            raise serializers.ValidationError(f"You must be at least 18 years old. your age is {age}")
        return value
    


class UserCreateSerializer(BaseUserCreateSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = LoginSystem
        fields = [
            'emp_id', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number',
            'profile_pictures', 'address', 'aadhar_number', 'pan_number', 'bank_name',
            'bank_account_number', 'bank_ifsc_code', 'is_doc_uploaded', 'password', 'is_staff' ,'is_superuser',
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
        if not re.match(r'^[a-zA-Z\s,.]+$', value) :
            raise serializers.ValidationError("First name can have only String ")
        # Additional checks can be added here (e.g., allowed characters)
        return value

    def validate_last_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Last name is required.")
        if len(value) > 100:
            raise serializers.ValidationError("Last name cannot exceed 100 characters.")
        if not re.match(r'^[a-zA-Z\s,.]+$', value) :
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

    def validate_date_of_birth(self, value):
        import datetime

        today = datetime.date.today()
        dob = value  # Ensure `value` is a datetime.date object
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            raise serializers.ValidationError(f"You must be at least 18 years old. Your age is {age}")
        return value

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

