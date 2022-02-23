from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import mixins, status

from api.v1.common.filters import filter_by_date_range
from api.v1.common.paginations import CustomPagination
from . import models, serializers


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('type', 'group')
    search_fields = ('title', 'model', 'code', 'type', 'group__title', 'currency__title',
                     'shelf_life', 'description', 'further')

    def get_queryset(self):
        params = self.request.query_params
        queryset = self.queryset.with_quantity(params.get('storage'))
        return queryset.order_by('id')


class ProductGroupViewSet(mixins.ListModelMixin,
                          GenericViewSet):
    queryset = models.ProductGroup.objects
    serializer_class = serializers.ProductGroupSerializer


class MeasurementUnitViewSet(mixins.ListModelMixin,
                             GenericViewSet):
    queryset = models.MeasurementUnit.objects
    serializer_class = serializers.MeasurementUnitSerializer


class StorageViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    queryset = models.Storage.objects
    serializer_class = serializers.StorageSerializer


class ProductOrderViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = models.ProductOrder.objects.all()
    serializer_class = serializers.ProductOrderSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid = serializer.validated_data

        if valid['type'] == 'plan':
            if valid['receive_invoice'] is not None or valid['leave_invoice'] is not None:
                return Response(
                    {
                        "success": False,
                        "message": "Given invalid data for product-order type plan!"
                    }, status.HTTP_400_BAD_REQUEST
                )
            storage = valid['storage']

        if valid['type'] == 'receive':
            if valid['receive_invoice'] is None or valid['leave_invoice'] is not None:
                return Response(
                    {
                        "success": False,
                        "message": "Given invalid data for product-order type receive!"
                    }, status.HTTP_400_BAD_REQUEST
                )
            storage = valid['receive_invoice'].storage

        if valid['type'] == 'leave':
            if valid['leave_invoice'] is None or valid['receive_invoice'] is not None:
                return Response(
                    {
                        "success": False,
                        "message": "Given invalid data for product-order type leave!"
                    }, status.HTTP_400_BAD_REQUEST
                )
            storage = valid['leave_invoice'].storage
            valid['quantity'] = -(valid['quantity'])
        
        product = valid['product']
        serializer.save(
            price=product.arrival_price, currency=product.currency, storage=storage
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = self.queryset
        queryset = filter_by_date_range(queryset, self.request.query_params)
        return queryset.order_by('-id')


class ReceiveInvoiceViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            GenericViewSet):
    queryset = models.ReceiveInvoice.objects.all()
    serializer_class = serializers.ReceiveInvoiceSerializer
    pagination_class = CustomPagination

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.status == 'saved':
            return Response(
                {
                    "success": False,
                    "message": "Can not update saved invoice"
                }, status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

    def get_queryset(self):
        queryset = self.queryset
        queryset = filter_by_date_range(queryset, self.request.query_params)
        return queryset.order_by('-id')


class LeaveInvoiceViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.UpdateModelMixin,
                          GenericViewSet):
    queryset = models.LeaveInvoice.objects.all()
    serializer_class = serializers.LeaveInvoiceSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.status == 'saved':
            return Response(
                {
                    "success": False,
                    "message": "Can not update saved invoice"
                }, status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

    def get_queryset(self):
        queryset = self.queryset
        queryset = filter_by_date_range(queryset, self.request.query_params)
        return queryset.order_by('-id')
