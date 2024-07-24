# viewsets.py
from rest_framework import viewsets
from .models import Identity_Card
from .serializers import IDCardSerializer

class IDCardViewSet(viewsets.ModelViewSet):
    queryset = Identity_Card.objects.all()
    serializer_class = IDCardSerializer
