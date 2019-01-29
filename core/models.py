import os
import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.conf import settings


def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)


class Profile(models.Model):
    """Class defining User object linked to profile by one-to-one"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    picture = models.ImageField(null=True, upload_to=recipe_image_file_path)


class Player(models.Model):
    nickname = models.CharField(max_length=255)
    win = models.IntegerField()
    loss = models.IntegerField()



class Gomoku_record(models.Model):
    record = models.CharField(max_length=255)
    game_date = models.DateTimeField()
    black_player = models.ForeignKey('Player')
    white_player = models.ForeignKey('Player')
    result = models.IntegerField()


