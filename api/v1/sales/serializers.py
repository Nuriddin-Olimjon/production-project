from rest_framework import serializers
from . import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = (
            'id',
            'title',
            'fullname',
            'phone_number',
            'city',
            'address',
            'bank_mfo',
            'bank_inn',
            'bank_account',
            'description'
        )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = (
            'id',
            'title'
        )
