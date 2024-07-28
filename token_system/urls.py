from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'token-order', views.TokenOrderViewSet)
router.register(r'token-order-item', views.TokenOrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
