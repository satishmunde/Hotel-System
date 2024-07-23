
from rest_framework import viewsets
from core.serializers import LoginSystemSerializer
from .models import *

# Create your views here.
class LoginSystemViewSet(viewsets.ModelViewSet):
    queryset = LoginSystem.objects.all()
    serializer_class = LoginSystemSerializer
    lookup_field = 'pk'

