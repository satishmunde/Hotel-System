
from rest_framework import viewsets
from core.serializers import LoginSystemSerializer
from .models import *

from rest_framework.response import Response  

# Create your views here.
class LoginSystemViewSet(viewsets.ModelViewSet):
    queryset = LoginSystem.objects.all()
    serializer_class = LoginSystemSerializer
    lookup_field = 'pk'

            
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
