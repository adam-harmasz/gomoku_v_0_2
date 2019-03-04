from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

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




