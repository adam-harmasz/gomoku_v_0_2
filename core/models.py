import os
import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from django.conf import settings
from django.db.models.signals import post_save

from core.signals import create_gomoku_record_object, update_player_stats


User = settings.AUTH_USER_MODEL


def profile_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/accounts/', filename)


def gomoku_record_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/gomoku_app/', filename)


class Profile(models.Model):
    """Class defining User object linked to profile by one-to-one"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    picture = models.ImageField(null=True, upload_to=profile_image_file_path)

    def __str__(self):
        return self.user


class Player(models.Model):
    """Class defining player object"""
    nickname = models.CharField(max_length=255, unique=True)
    win = models.FloatField(default=0, blank=True, null=True)
    loss = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return self.nickname


class GomokuRecord(models.Model):
    """Class defining gomoku record object"""
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    game_record = models.TextField()
    game_date = models.DateTimeField()
    black_player = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
        related_name='black_player'
    )
    white_player = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
        related_name='white_player'
    )
    result = models.CharField(max_length=50)
    swap = models.BooleanField()
    swap_2 = models.BooleanField()
    color_change = models.BooleanField()

    def __str__(self):
        return f'{self.black_player} - {self.white_player}'


class GomokuRecordFile(models.Model):
    """Class defining GomokuRecordFiles objects"""
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    game_record_file = models.FileField(
        null=True,
        upload_to=gomoku_record_image_file_path
    )

    def __str__(self):
        return f'game record owned by: {self.profile}'


# Signals to create gomoku record and update players data
post_save.connect(create_gomoku_record_object, sender=GomokuRecordFile)
post_save.connect(update_player_stats, sender=GomokuRecord)
