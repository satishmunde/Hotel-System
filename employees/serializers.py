from datetime import datetime
import re
from rest_framework import serializers
from .models import Department, Document, Position, EmployeePosition, RequiredDocument,EmployeePayment


# Regex patterns for validation
ALPHA_ONLY_PATTERN = re.compile(r'^[a-zA-Z\s]+$')
SAFE_FILENAME_PATTERN = re.compile(r'^[\w\-. ]+$')  # Only allow alphanumeric, underscores, hyphens, dots, and spaces
MIN_LENGTH = 1
MAX_LENGTH = 100


class EmployeePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePayment
        fields = '__all__'
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    def validate_payment_date(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Payment date cannot be in the future.")
        return value


class DepartmentSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        # Clean the data
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Name is required.")
        if len(value) > MAX_LENGTH:
            raise serializers.ValidationError(f"Name must be at most {MAX_LENGTH} characters long.")
        if not ALPHA_ONLY_PATTERN.match(value):
            raise serializers.ValidationError("Name can only contain alphabetic characters and spaces.")
        if Department.objects.filter(name=value).exists():
            raise serializers.ValidationError("A Department  already exists.")
        return value
    
    

    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['dept_id', 'is_active']

class DocumentSerializer(serializers.ModelSerializer):
    def validate_document_type(self, value):
        # Clean the data
        value = value.strip()
        
        
        if not value:
            raise serializers.ValidationError("Document type is required.")
        if len(value) > MAX_LENGTH:
            raise serializers.ValidationError(f"Document type must be at most {MAX_LENGTH} characters long.")
        if not ALPHA_ONLY_PATTERN.match(value):
            raise serializers.ValidationError("Document type can only contain alphabetic characters and spaces.")
        
        
        return value
    
    def validate(self, data):
        # Check if the combination of employee and document_type already exists
        employee = data.get('employee')
        document_type = data.get('document_type')

        if Document.objects.filter(employee=employee, document_type=document_type).exists():
            raise serializers.ValidationError("A document with this employee and document type already exists.")

        return data


    def validate_document(self, value):
        # Check file type and name
        if not value.name.endswith(('.pdf',  '.jpg')):
            raise serializers.ValidationError("Unsupported file format. Please upload a PDF, or JPG file.")
        # if not SAFE_FILENAME_PATTERN.match(value.name):
        #     raise serializers.ValidationError("File name contains invalid characters.")
        return value

    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ['is_active']

class PositionSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        # Clean the data
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Position name is required.")
        if len(value) > MAX_LENGTH:
            raise serializers.ValidationError(f"Position name must be at most {MAX_LENGTH} characters long.")
        if not ALPHA_ONLY_PATTERN.match(value):
            raise serializers.ValidationError("Position name can only contain alphabetic characters and spaces.")
        if Position.objects.filter(name=value).exists():
            raise serializers.ValidationError("A Position already exists.")

     

        return value

    class Meta:
        model = Position
        fields = '__all__'
        read_only_fields = ['is_active']

class EmployeePositionSerializer(serializers.ModelSerializer):
    
    def validate_employee(self, value):
        # Check if the employee exists
        if not value:
            raise serializers.ValidationError("Employee must be specified.")
        # Assuming `AUTH_USER_MODEL` is the model for employees, you can check if the employee exists
        # This validation depends on your specific user model, adjust accordingly
        if not value.pk:  # Replace with appropriate check if necessary
            raise serializers.ValidationError("Employee does not exist.")
        return value

    def validate_department(self, value):
        # Check if the department exists
        if not value:
            raise serializers.ValidationError("Department must be specified.")
        if not Department.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError("Department does not exist.")
        return value

    def validate_position(self, value):
        # Check if the position exists
        if not value:
            raise serializers.ValidationError("Position must be specified.")
        if not Position.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError("Position does not exist.")
        return value




    def validate(self, data):
        # Additional cross-field validation
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        employee = data.get('employee')
        department = data.get('department')
        position = data.get('position')

        # Check if end_date is before start_date
        if end_date and start_date and end_date < start_date:
            raise serializers.ValidationError("End date cannot be before start date.")

        # Check if an identical record already exists
        existing_entries = EmployeePosition.objects.filter(
            employee=employee,
            department=department,
            position=position
        ).exclude(pk=self.instance.pk if self.instance else None)

        if existing_entries.exists():
            raise serializers.ValidationError("An EmployeePosition with this employee, department, and position already exists.")

        return data
    

    class Meta:
        model = EmployeePosition
        fields = '__all__'
        read_only_fields = ['is_active']


class RequiredDocumentsSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        # Clean the data
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Document name is required.")
        if len(value) > MAX_LENGTH:
            raise serializers.ValidationError(f"Document name must be at most {MAX_LENGTH} characters long.")
        if not ALPHA_ONLY_PATTERN.match(value):
            raise serializers.ValidationError("Document name can only contain alphabetic characters and spaces.")
        if RequiredDocument.objects.filter(name=value).exists():
            raise serializers.ValidationError("This Document Name already exists.")


        return value
    
    class Meta:
        model = RequiredDocument
        fields = '__all__'
        read_only_fields = ['is_active']
