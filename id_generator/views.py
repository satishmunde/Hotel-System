# viewsets.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Identity_Card 
from .serializers import IDCardSerializer
from rest_framework import permissions
from .filters import Identity_CardFilter
from django_filters.rest_framework import DjangoFilterBackend

class IDCardViewSet(viewsets.ModelViewSet):
    queryset = Identity_Card.objects.all()
    serializer_class = IDCardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = Identity_CardFilter
    permission_classes = [permissions.IsAuthenticated]

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
