# viewsets.py
from rest_framework import viewsets
from .models import Identity_Card
from rest_framework.response import Response  
from .serializers import IDCardSerializer

class IDCardViewSet(viewsets.ModelViewSet):
    queryset = Identity_Card.objects.all()
    serializer_class = IDCardSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

