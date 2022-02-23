from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    quantity = serializers.ReadOnlyField()

    class Meta:
        model = models.Product
        fields = (
            'id',
            'title',
            'model',
            'code',
            'type',
            'group',
            'measurement_unit',
            'arrival_price',
            'selling_price',
            'currency',
            'shelf_life',
            'critical_quantity',
            'description',
            'further',
            'time_created',
            'time_updated',

            'quantity',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['group'] = instance.group.title
        data['measurement_unit'] = instance.measurement_unit.title
        data['currency'] = instance.currency.title
        return data


class ProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductGroup
        fields = (
            'id',
            'title'
        )


class MeasurementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MeasurementUnit
        fields = (
            'id',
            'title'
        )

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Storage
        fields = (
            'id',
            'title',
            'address'
        )


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductOrder
        fields = (
            'id',
            'type',
            'receive_invoice',
            'leave_invoice',
            'product',
            'quantity',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product'] = instance.product.title
        data['currency'] = instance.currency.title
        data['price'] = instance.price
        data['storage'] = instance.storage.title
        return data


class ReceiveInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReceiveInvoice
        fields = (
            'id',
            'supplier',
            'storage',
            'responsible',
            'status',
            'description',
            'further',
            'time_created',
            'time_updated'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['supplier'] = instance.supplier.title
        data['storage'] = instance.storage.title
        return data


class LeaveInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeaveInvoice
        fields = (
            'id',
            'storage',
            'client',
            'deadline',
            'responsible',
            'status',
            'description',
            'further',
            'time_created',
            'time_updated'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['storage'] = instance.storage.title
        data['client'] = instance.client.title
        data['created_by'] = f"{instance.created_by.first_name} {instance.created_by.last_name}"
        return data


class DefectiveProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DefectiveProduct
        fields = (
            'id',
            'product',
            'quantity',
            'valid_status',
            'returned_status'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product'] = instance.product.title
        return data
