from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register("client", views.ClientViewSet)
router.register("city", views.CityViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
