from rest_framework import serializers
from . import models


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Income
        fields = (
            'id',
            'cashbox',
            'type',
            'client',
            'extra_income_title',
            'payment_type',
            'total_sum',
            'currency',
            'description',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['cashbox'] = instance.cashbox.title
        if instance.client is not None:
            data['client'] = instance.client.title
        data['currency'] = instance.currency.title
        return data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = (
            'id',
            'cost_type',
            'cashbox',
            'to_where',
            'supplier',
            'employee',
            'sub_cost_type',
            'bonus',
            'bonus_reason',
            'fine',
            'fine_reason',
            'payment_type',
            'total_sum',
            'currency',
            'description'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['cost_type'] = instance.cost_type.title
        data['cashbox'] = instance.cashbox.title
        if instance.supplier is not None:
            data['supplier'] = instance.supplier.title
        if instance.employee is not None:
            data['employee'] = f"{instance.employee.first_name} {instance.employee.last_name}"
        if instance.sub_cost_type is not None:
            data['sub_cost_type'] = instance.sub_cost_type.title
        data['currency'] = instance.currency.title
        return data


class CostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CostType
        fields = (
            'id',
            'title',
            'to_supplier',
            'to_employee'
        )


class SubCostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCostType
        fields = (
            'id',
            'type',
            'title'
        )


class CashboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cashbox
        fields = (
            'id',
            'title',
            'cashier'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['cashier'] = f"{instance.cashier.first_name} {instance.cashier.last_name}"


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = (
            'id',
            'title'
        )