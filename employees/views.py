# viewsets.py
from rest_framework.response import Response  
from rest_framework import viewsets
from .models import Department, Employee, Position, EmployeePosition ,RequiredDocument,Document
from .serializers import DepartmentSerializer, EmployeeSerializer, PositionSerializer, EmployeePositionSerializer ,RequireDocumentsSerializer,DocumentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

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


