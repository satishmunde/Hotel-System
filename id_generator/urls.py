# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IDCardViewSet

router = DefaultRouter()
router.register(r'idcards', IDCardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # other paths in your urlpatterns
]
