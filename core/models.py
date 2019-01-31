import os
import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.conf import settings
from django.urls import reverse_lazy


def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/gomoku_app/', filename)


class Profile(models.Model):
    """Class defining User object linked to profile by one-to-one"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    picture = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self):
        return self.user

    # def get_absolute_url(self, request):
    #     return reverse_lazy(
    #         'profiles:detail',
    #         kwargs={'username': self.user.username}
    #     )


class Player(models.Model):
    """Class defining player object"""
    nickname = models.CharField(max_length=255)
    win = models.IntegerField()
    loss = models.IntegerField()

    def __str__(self):
        return self.nickname


class GomokuRecord(models.Model):
    """Class defining gomoku record object"""
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    record = models.CharField(max_length=255)
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
    result = models.IntegerField()
    swap = models.BooleanField()
    swap_2 = models.BooleanField()
    color_change = models.BooleanField()

    def __str__(self):
        return f'{self.black_player} - {self.white_player}'



