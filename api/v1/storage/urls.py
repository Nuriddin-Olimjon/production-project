from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register("product", views.ProductViewSet)
router.register("product-group", views.ProductGroupViewSet)
router.register("measurement-unit", views.MeasurementUnitViewSet)
router.register("storage", views.StorageViewSet)
router.register("product-order", views.ProductOrderViewSet)
router.register("receive-invoice", views.ReceiveInvoiceViewSet)
router.register("leave-invoice", views.LeaveInvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
