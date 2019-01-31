from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from django.contrib.auth import get_user_model

from . import serializers

User = get_user_model()


class UserViewset(viewsets.ModelViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer