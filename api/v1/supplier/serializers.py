from rest_framework import serializers
from . import models


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Supplier
        fields = (
            'id',
            'title',
            'fullname',
            'phone_number1',
            'phone_number2',
            'responsible',
            'address',
            'bank_mfo',
            'bank_inn',
            'bank_account',
            'description'
        )
