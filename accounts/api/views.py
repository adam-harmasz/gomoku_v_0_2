from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from django.contrib.auth import get_user_model
from rest_framework import permissions

from core import models
from . import serializers

User = get_user_model()


class UserViewset(viewsets.ModelViewSet):
    """User objects Viewset"""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileViewset(viewsets.ModelViewSet):
    """Profile objects Viewset"""
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
