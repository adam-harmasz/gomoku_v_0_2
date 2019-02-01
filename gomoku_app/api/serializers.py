from rest_framework import serializers
from django.contrib.auth import get_user_model

from core import models

User = get_user_model()


class GomokuRecordSerializer(serializers.ModelSerializer):
    """serializers to handle GameRecord object"""

    class Meta:
        model = models.GomokuRecord
        fields = (
            'id',
            'profile',
            'game_record',
            'game_date',
            'black_player',
            'white_player',
            'result',
            'swap',
            'swap_2',
            'color_change'
        )
        read_only_fields = ('id',)
