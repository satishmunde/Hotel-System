# filters.py
import django_filters
from .models import EmployeePayment, Department, Position, EmployeePosition, RequiredDocument, Document

class EmployeePaymentFilter(django_filters.FilterSet):
    class Meta:
        model = EmployeePayment
        fields = ['employee','payment_date','payment_method',]
        # fields = '__all__'
        

class DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department
        fields = '__all__'

class PositionFilter(django_filters.FilterSet):
    class Meta:
        model = Position
        fields = '__all__'

class EmployeePositionFilter(django_filters.FilterSet):
    class Meta:
        model = EmployeePosition
        fields = '__all__'

class RequiredDocumentFilter(django_filters.FilterSet):
    class Meta:
        model = RequiredDocument
        fields = '__all__'

class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = Document
        fields = ['employee','document_type','uploaded_at']
