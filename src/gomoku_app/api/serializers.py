"""Serializers for Gomoku App API"""
from rest_framework import serializers

from core import models


class GomokuRecordSerializer(serializers.ModelSerializer):
    """serializers to handle GameRecord object"""

    black_player_nickname = serializers.SerializerMethodField()
    white_player_nickname = serializers.SerializerMethodField()

    class Meta:
        """Specifying model and fields for serializer"""
        model = models.GomokuRecord
        fields = (
            "id",
            "profile",
            "game_record",
            "game_date",
            "black_player",
            "white_player",
            "result",
            "swap",
            "swap_2",
            "color_change",
            "black_player_nickname",
            "white_player_nickname",
        )
        read_only_fields = ("id",)

    def get_black_player_nickname(self, obj):
        """Get black player nickname from obj for serializer field"""
        return obj.black_player.nickname

    def get_white_player_nickname(self, obj):
        """Get white player nickname from obj for serializer field"""
        return obj.white_player.nickname
