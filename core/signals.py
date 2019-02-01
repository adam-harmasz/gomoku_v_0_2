from django.contrib.auth import get_user_model

from core.utils import extract_data_from_game_record_file
from core import models


def create_gomoku_record_object(sender, instance, created, **kwargs):
    """
    Signal to create players and game record object after file is uploaded
    """
    if created:
        payload = extract_data_from_game_record_file(
            f'config/media/{instance.game_record_file}'
        )
        models.Player.objects.get_or_create(
            nickname=payload['white'],
        )
        models.Player.objects.get_or_create(
            nickname=payload['black'],
        )
        white_player = models.Player.objects.get(nickname=payload['white'])
        black_player = models.Player.objects.get(nickname=payload['black'])

        models.GomokuRecord.objects.create(
            profile=get_user_model().objects.get(username=instance.profile),
            game_record=payload['game_record'],
            game_date=payload['game_date'],
            result=payload['result'],
            swap=payload['swap'],
            swap_2=payload['swap_2'],
            color_change=payload['color_change'],
            black_player=black_player,
            white_player=white_player,
        )


def update_player_stats(sender, instance, created, **kwargs):
    """Signal to update player win/loss"""
    if created:
        black_player = models.Player.objects.get(
            nickname=instance.black_player
        )
        white_player = models.Player.objects.get(
            nickname=instance.white_player
        )
        result = instance.result
        if result == 'black':
            black_player.win += 1
            white_player.loss += 1
            black_player.save()
            white_player.save()
        elif result == 'white':
            black_player.loss += 1
            white_player.win += 1
            black_player.save()
            white_player.save()
        elif result == 'draw':
            black_player.win += 0.5
            white_player.win += 0.5
            black_player.save()
            white_player.save()
        else:
            raise ValueError('wrong data in instance.result')
