from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from core import models

User = get_user_model()


class GomokuRecordFileSerializer(serializers.ModelSerializer):
    """serializers to handle file object and help with extracting data"""

    class Meta:
        model = models.GomokuRecordFile
        fields = ('id', 'game_record_file', 'url')
        read_only_fields = ('id',)

    # def save(self):
    #     profile = self.context['request'].user
    #     game_record_file = self.validated_data['game_record_file']
    #     url = self.validated_data['url']
    #     print(profile, game_record_file, url)

    def create(self, validated_data):
        user = self.context['request'].user
        game_record_file = validated_data['game_record_file']
        print(user, validated_data['game_record_file'])
        profile = CurrentUserDefault()
        return models.GomokuRecordFile.objects.create(
            profile=user,
            status='file',
            game_record_file=game_record_file)
