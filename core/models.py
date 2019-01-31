import os
import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse_lazy


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
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    picture = models.ImageField(null=True, upload_to=profile_image_file_path)

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
    result = models.IntegerField()
    swap = models.BooleanField()
    swap_2 = models.BooleanField()
    color_change = models.BooleanField()

    def __str__(self):
        return f'{self.black_player} - {self.white_player}'


class GomokuRecordFile(models.Model):
    """Class defining GomokuRecordFiles objects"""
    game_record_file = models.FileField(
        null=True,
        upload_to=gomoku_record_image_file_path
    )
    # file_path = models.CharField(max_length=255, default=None, null=True)


# @receiver(post_save, sender=GomokuRecordFile)
# def create_gomoku_record_object_profile(sender, instance, created, **kwargs):
#     if created:
#         # Parent.objects.create(name_of_parent=instance)
#         pass
#
#
# @receiver(post_save, sender=GomokuRecordFile)
# def save_user_profile(sender, instance, **kwargs):
#     instance.parent.save()




