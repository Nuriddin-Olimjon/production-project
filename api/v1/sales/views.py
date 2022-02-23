from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from . import models, serializers


class ClientViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = models.Client.objects
    serializer_class = serializers.ClientSerializer


class CityViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = models.City.objects
    serializer_class = serializers.CitySerializer
