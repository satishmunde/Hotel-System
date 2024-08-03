# viewsets.py
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import TokenOrder, TokenOrderItem
from .serializers import TokenOrderSerializer, TokenOrderItemSerializer
from .filters import TokenOrderFilter, TokenOrderItemFilter

class TokenOrderViewSet(viewsets.ModelViewSet):
    queryset = TokenOrder.objects.all()
    serializer_class = TokenOrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add permissions
    filter_backends = [DjangoFilterBackend]
    filterset_class = TokenOrderFilter  # Add filtering

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).filter()
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

class TokenOrderItemViewSet(viewsets.ModelViewSet):
    queryset = TokenOrderItem.objects.all()
    serializer_class = TokenOrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add permissions
    filter_backends = [DjangoFilterBackend]
    filterset_class = TokenOrderItemFilter  # Add filtering

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).filter()
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
