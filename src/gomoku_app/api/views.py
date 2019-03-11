from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model

from .pagination import StandardResultsPagination
from . import serializers
from core import models

User = get_user_model()


class GomokuRecordViewset(viewsets.ModelViewSet):
    """Viewset to handle serialized GameRecord objects data"""

    queryset = models.GomokuRecord.objects.all()
    serializer_class = serializers.GomokuRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsPagination