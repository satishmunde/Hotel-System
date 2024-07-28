from rest_framework import viewsets
from .models import TokenOrderItem, TokenOrder
from .serializers import TokenOrderSerializer,TokenOrderItemSerializer


class TokenOrderViewSet(viewsets.ModelViewSet):
    queryset = TokenOrder.objects.all()
    serializer_class = TokenOrderSerializer
    
class TokenOrderItemViewSet(viewsets.ModelViewSet):
    queryset = TokenOrderItem.objects.all()
    serializer_class = TokenOrderItemSerializer
