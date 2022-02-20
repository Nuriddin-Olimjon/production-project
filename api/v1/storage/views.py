from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import mixins, status

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data['product']
        serializer.save(price=product.arrival_price, currency=product.currency)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LeaveInvoiceViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = models.LeaveInvoice.objects
    serializer_class = serializers.LeaveInvoiceSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LeaveInvoiceOrderViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               GenericViewSet):
    queryset = models.LeaveInvoiceOrder.objects
    serializer_class = serializers.LeaveInvoiceOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data['product']
        serializer.save(price=product.arrival_price, currency=product.currency)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
