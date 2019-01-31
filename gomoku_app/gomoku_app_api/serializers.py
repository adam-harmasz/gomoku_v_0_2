from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from core import models

User = get_user_model()


class GomokuRecordFileSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipes"""

    class Meta:
        model = models.GomokuRecord
        fields = ('id', 'gomoku_record_file')
        read_only_fields = ('id',)

