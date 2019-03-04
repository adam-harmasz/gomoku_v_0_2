from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from core import models

User = get_user_model()


class GomokuRecordSerializer(serializers.ModelSerializer):
    """serializers to handle GameRecord object"""
    black_player_nickname = serializers.SerializerMethodField()
    white_player_nickname = serializers.SerializerMethodField()

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
            'color_change',
            'black_player_nickname',
            'white_player_nickname'
        )
        read_only_fields = ('id',)

    def get_black_player_nickname(self, obj):
        return obj.black_player.nickname

    def get_white_player_nickname(self, obj):
        return obj.white_player.nickname
