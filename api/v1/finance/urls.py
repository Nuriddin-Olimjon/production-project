from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register("income", views.IncomeViewSet)
router.register("payment", views.PaymentViewSet)
router.register("cost-type", views.CostTypeViewSet)
router.register("sub-cost-type", views.SubCostTypeViewSet)
router.register("cashbox", views.CashboxViewSet)
router.register("currency", views.CurrencyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
