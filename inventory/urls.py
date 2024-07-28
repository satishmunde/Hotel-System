from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InventoryItemViewSet,
    SupplierViewSet,
    PurchaseOrderViewSet,
    PurchaseOrderItemViewSet,
    ExpenseViewSet
)

router = DefaultRouter()
router.register(r'inventoryitems', InventoryItemViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'purchaseorders', PurchaseOrderViewSet)
router.register(r'purchaseorderitems', PurchaseOrderItemViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
