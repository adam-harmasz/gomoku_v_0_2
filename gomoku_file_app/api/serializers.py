from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from core import models

User = get_user_model()


class GomokuRecordFileSerializer(serializers.ModelSerializer):
    """serializers to handle file object and help with extracting data"""

    class Meta:
        model = models.GomokuRecordFile
        fields = ('id', 'gomoku_record_file')
        read_only_fields = ('id',)
