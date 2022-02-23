from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from . import models, serializers


class SupplierViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = models.Supplier.objects
    serializer_class = serializers.SupplierSerializer
