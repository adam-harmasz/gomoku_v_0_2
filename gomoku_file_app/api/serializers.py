from rest_framework import serializers
from django.contrib.auth import get_user_model

from core import models
from core.utils import check_domain

User = get_user_model()


class GomokuRecordFileSerializer(serializers.ModelSerializer):
    """serializers to handle file object and help with extracting data"""

    class Meta:
        model = models.GomokuRecordFile
        fields = ('id', 'game_record_file', 'url')
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Creating GameRecordFile object"""
        status = None
        user = self.context['request'].user
        url = validated_data.get('url')
        game_record_file = validated_data.get('game_record_file')
        if game_record_file:
            status = 'file'
        elif url:
            status = 'url'
        if status is None:
            raise serializers.ValidationError('Status must be url or file')
        return models.GomokuRecordFile.objects.create(
            url=url,
            profile=user,
            status=status,
            game_record_file=game_record_file)

    def validate_game_record_file(self, attrs):
        """File validation"""
        if str(attrs).endswith('.txt'):
            return attrs
        raise serializers.ValidationError(
            'Wrong type of file, only txt type file allowed')

    def validate_url(self, attrs):
        """File validation"""
        allowed_domains = ('https://www.kurnik.pl', 'https://www.playok.com')
        print(check_domain(attrs))
        if check_domain(attrs) in allowed_domains and attrs[-3:] == 'txt':
            return attrs
        raise serializers.ValidationError('Invalid url, only games from kurnik.pl'
                                     ' or playok.com are allowed')
