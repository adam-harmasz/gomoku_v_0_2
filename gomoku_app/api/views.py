from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from django.contrib.auth import get_user_model

from . import serializers
from core import models

User = get_user_model()


class GomokuRecordViewset(viewsets.ModelViewSet):
    queryset = models.GomokuRecord.objects.all()
    serializer_class = serializers.GomokuRecordFileSerializer

