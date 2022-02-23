from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins, status
from api.v1.common.filters import filter_by_date_range
from api.v1.common.paginations import CustomPagination

from . import models, serializers


class IncomeViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = models.Income.objects.all()
    serializer_class = serializers.IncomeSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid = serializer.validated_data

        if valid['type'] == 'client':
            if valid['client'] is None or valid['extra_income_title'] != '':
                return Response(
                    {
                        "success": "False",
                        "message": "Given invalid data for income type client"
                    }, status.HTTP_400_BAD_REQUEST
                )

        if valid['type'] == 'extra':
            if valid['client'] is not None or valid['extra_income_title'] == '':
                return Response(
                    {
                        "success": False,
                        "message": "Given invalid data for income type extra"
                    }, status.HTTP_400_BAD_REQUEST
                )

        serializer.save(created_by=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = self.queryset
        queryset = filter_by_date_range(queryset, self.request.query_params)
        return queryset.order_by('-id')


class PaymentViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid = serializer.validated_data

        if valid['cost_type'].to_supplier is True:
            if valid['supplier'] is None or valid['employee'] is not None or valid['sub_cost_type'] is not None:
                return Response(
                    {
                        "success": False,
                        "message": "Given invalid data for payment type to_supplier"
                    }, status.HTTP_400_BAD_REQUEST
                )

        if valid['cost_type'].to_employee is True:
            if valid['supplier'] is not None or valid['employee'] is None or valid['sub_cost_type'] is not None:
                return Response(
                    {
                        "success": False,
                        "message": "Given invalid data for payment type to_employee"
                    }, status.HTTP_400_BAD_REQUEST
                )

        if valid['cost_type'].to_supplier is False and valid['cost_type'].to_employee is False:
            if valid['supplier'] is not None or valid['employee'] is not None or valid['sub_cost_type'] is None:
                return Response(
                    {
                        "success": False,
                        "message": "Given invalid data for payment"
                    }, status.HTTP_400_BAD_REQUEST
                )

        serializer.save(created_by=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = self.queryset
        queryset = filter_by_date_range(queryset, self.request.query_params)
        return queryset.order_by('-id')


class CostTypeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = models.CostType.objects
    serializer_class = serializers.CostTypeSerializer


class SubCostTypeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = models.SubCostType.objects
    serializer_class = serializers.SubCostTypeSerializer


class CashboxViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = models.Cashbox.objects
    serializer_class = serializers.CashboxSerializer


class CurrencyViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = models.Currency.objects
    serializer_class = serializers.CurrencySerializer
