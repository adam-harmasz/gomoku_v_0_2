from rest_framework import serializers
from django.contrib.auth import get_user_model

from core import models

User = get_user_model()


class PlayerSerializer(serializers.ModelSerializer):
    """Serializer to handle Player object"""

    class Meta:
        model = models.Player
        fields = ("id", "nickname", "win", "loss")
        read_only_fields = ("id",)
