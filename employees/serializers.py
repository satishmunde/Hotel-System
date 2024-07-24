# serializers.py
from rest_framework import serializers
from .models import Department, Employee, Position, EmployeePosition,Document ,RequiredDocument

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True)  # For reverse relation

    class Meta:
        model = Employee
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EmployeePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePosition
        fields = '__all__'

class RequireDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredDocument
        fields = '__all__'

