from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import LoginSystem
from .serializers import LoginSystemSerializer

class LoginSystemViewSet(viewsets.ModelViewSet):
    queryset = LoginSystem.objects.all()
    serializer_class = LoginSystemSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Enable partial updates
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
