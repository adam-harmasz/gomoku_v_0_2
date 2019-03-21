"""API views for Gomoku app"""
from rest_framework import viewsets
from rest_framework import permissions

from core import models
from .pagination import StandardResultsPagination
from . import serializers


class GomokuRecordViewset(viewsets.ModelViewSet):
    """Viewset to handle serialized GameRecord objects data"""

    queryset = models.GomokuRecord.objects.all()
    serializer_class = serializers.GomokuRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsPagination
