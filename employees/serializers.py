
from rest_framework import serializers
from .models import Department,Document,Position,EmployeePosition,RequiredDocument

class DepartmentSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Check for existing department name
        if 'name' in self.partial:
            name = data.get('name')
            if name and Department.objects.filter(name=name).exclude(dept_id=self.instance.dept_id).exists():
                raise serializers.ValidationError("Department name already exists.")
        
        return data
    
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['dept_id', 'is_active']

class DocumentSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Check for valid foreign key reference
        if 'employee' in self.partial:
            employee_id = data.get('employee')
            if employee_id and not Document.objects.filter(employee_id=employee_id ,document_type=document_type).exists():
                raise serializers.ValidationError("Invalid employee ID.")
        
        # Ensure document_type is not empty
        if 'document_type' in self.partial:
            document_type = data.get('document_type')
            if not document_type:
                raise serializers.ValidationError("Document type cannot be empty.")
        
        return data
    
    def update(self, instance, validated_data):
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
        # Check for existing position name
        if 'name' in self.partial:
            name = data.get('name')
            if name and Position.objects.filter(name=name).exclude(pos_id=self.instance.pos_id).exists():
                raise serializers.ValidationError("Position already exists.")
        
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
        # Validate foreign key references
        if 'employee' in self.partial:
            employee_id = data.get('employee')
            if employee_id and not EmployeePosition.objects.filter(employee_id=employee_id).exists():
                raise serializers.ValidationError("Invalid employee ID.")
        
        if 'department' in self.partial:
            department_id = data.get('department')
            if department_id and not EmployeePosition.objects.filter(department_id=department_id).exists():
                raise serializers.ValidationError("Invalid department ID.")
        
        if 'position' in self.partial:
            position_id = data.get('position')
            if position_id and not EmployeePosition.objects.filter(position_id=position_id).exists():
                raise serializers.ValidationError("Invalid position ID.")
        
        # Ensure start_date is provided and in the correct format
        if 'start_date' in self.partial:
            start_date = data.get('start_date')
            if not start_date:
                raise serializers.ValidationError("Start date cannot be empty.")
        
        return data
    
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    class Meta:
        model = EmployeePosition
        fields = '__all__'
        read_only_fields = ['is_active']

class RequiredDocumentsSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Ensure name is not empty
        if 'name' in self.partial:
            name = data.get('name')
            if not name:
                raise serializers.ValidationError("Name cannot be empty.")
        
        return data
    
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    class Meta:
        model = RequiredDocument
        fields = '__all__'
        read_only_fields = ['is_active']
