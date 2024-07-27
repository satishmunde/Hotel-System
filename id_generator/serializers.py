import re
from rest_framework import serializers
from .models import Identity_Card

# Regex patterns for file name validation
SAFE_FILENAME_PATTERN = re.compile(r'^[\w\-. ]+$')  # Only allow alphanumeric, underscores, hyphens, dots, and spaces

class IDCardSerializer(serializers.ModelSerializer):
    
    def validate_employee(self, value):
        # Check if the employee exists
        if not value:
            raise serializers.ValidationError("Employee must be specified.")
        if not value.pk:  # Adjust based on your actual user model validation
            raise serializers.ValidationError("Employee does not exist.")
        return value

    def validate_card_pdf(self, value):
        # Check file type and name
        if not value.name.endswith('.pdf'):
            raise serializers.ValidationError("Unsupported file format. Please upload a PDF file.")
        if not SAFE_FILENAME_PATTERN.match(value.name):
            raise serializers.ValidationError("File name contains invalid characters.")
        return value

    def validate(self, data):
        """
        Check if an Identity_Card with the same employee and card_pdf already exists.
        """
        employee = data.get('employee')
        card_pdf = data.get('card_pdf')

        # Ensure that the `card_pdf` is a file instance for checking existing records
        if not isinstance(card_pdf, str):  # Handle file uploads
            existing_records = Identity_Card.objects.filter(
                employee=employee,
                card_pdf=card_pdf
            ).exclude(pk=self.instance.pk if self.instance else None)
            
            if existing_records.exists():
                raise serializers.ValidationError("An ID card with this employee and card file already exists.")

        return data

    class Meta:
        model = Identity_Card
        fields = '__all__'
        read_only_fields = ['created_at', 'is_active']
