from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
