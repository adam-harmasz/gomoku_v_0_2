from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model

from . import serializers
from core import models

User = get_user_model()


class PlayerViewset(viewsets.ModelViewSet):
    """Viewset to handle data from PlayerSerializer"""

    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]
