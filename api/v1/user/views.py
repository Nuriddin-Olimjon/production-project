from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import mixins, status
from rest_framework_simplejwt.views import TokenObtainPairView

from . import models, serializers
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterUserView(mixins.CreateModelMixin, GenericViewSet):
    queryset = models.User.objects
    serializer_class = serializers.RegisterUserSerializer
    # permission_classes = ()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "message": "Error occurred",
                    "error": serializer.errors,
                    "data": {},
                }, status.HTTP_400_BAD_REQUEST
            )
        self.perform_create(serializer)
        return Response(
            {
                "success": True,
                "message": "Registration successfully",
                "error": [],
                "data": serializer.data,
            }, status.HTTP_201_CREATED
        )

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
