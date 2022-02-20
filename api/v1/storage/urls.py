from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register("product", views.ProductViewSet)
router.register("receive-invoice", views.ReceiveInvoiceViewSet)
router.register("receive-invoice-order", views.ReceiveInvoiceOrderViewSet)
router.register("leave-invoice", views.LeaveInvoiceViewSet)
router.register("leave-invoice-order", views.LeaveInvoiceOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
