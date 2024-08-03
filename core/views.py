
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import LoginSystem
from .serializers import LoginSystemSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, permissions
from .models import LoginSystem
from .filters import LoginSystemFilter  # Import filter class if needed

class LoginSystemViewSet(viewsets.ModelViewSet):
    queryset = LoginSystem.objects.all()
    serializer_class = LoginSystemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add permissions
    filter_backends = [DjangoFilterBackend]  # Add filtering
    filterset_class = LoginSystemFilter  # Use the filter class if needed

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).filter()
        print(queryset.query)  # Print the SQL query to check if filtering is applied
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



    def retrieve(self, request, pk=None):
        
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
