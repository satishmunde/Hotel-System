# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)

router.register(r'positions', views.PositionViewSet)
router.register(r'employeepositions', views.EmployeePositionViewSet)
router.register(r'req-docs', views.RequiredDocumentViewSet)
router.register(r'documents', views.DocumentViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
