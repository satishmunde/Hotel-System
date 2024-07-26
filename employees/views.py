# viewsets.py
from rest_framework.response import Response  
from rest_framework import viewsets
from .models import Department, Position, EmployeePosition ,RequiredDocument,Document
from .serializers import DepartmentSerializer, PositionSerializer, EmployeePositionSerializer ,RequireDocumentsSerializer,DocumentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer



class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class EmployeePositionViewSet(viewsets.ModelViewSet):
    queryset = EmployeePosition.objects.all()
    serializer_class = EmployeePositionSerializer
    

class RequiredDocumentViewSet(viewsets.ModelViewSet):
    queryset = RequiredDocument.objects.all()
    serializer_class = RequireDocumentsSerializer



class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


