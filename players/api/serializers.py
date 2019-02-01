from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from core import models

User = get_user_model()