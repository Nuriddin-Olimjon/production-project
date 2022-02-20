from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter
from rest_framework import mixins

from . import models, serializers


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = models.Product.objects.with_quantity()
    serializer_class = serializers.ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_fields = ('type', 'group__title', 'storage__title')


class ReceiveInvoiceViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):
    queryset = models.ReceiveInvoice.objects
    serializer_class = serializers.ReceiveInvoiceSerializer


class ReceiveInvoiceOrderViewSet(mixins.CreateModelMixin,
                                 mixins.ListModelMixin,
                                 GenericViewSet):
    queryset = models.ReceiveInvoiceOrder.objects
    serializer_class = serializers.ReceiveInvoiceOrderSerializer


class LeaveInvoiceViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = models.LeaveInvoice.objects
    serializer_class = serializers.LeaveInvoiceSerializer
    

class LeaveInvoiceOrderViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               GenericViewSet):
    queryset = models.LeaveInvoiceOrder.objects
    serializer_class = serializers.LeaveInvoiceOrderSerializer
