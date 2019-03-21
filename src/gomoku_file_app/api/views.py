"""API views for gomoku_file_app"""
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from core import models
from . import serializers


class GomokuRecordImageViewset(viewsets.ModelViewSet):
    """Viewset to handle uploading file with game record"""

    serializer_class = serializers.GomokuRecordFileSerializer
    queryset = models.GomokuRecordFile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()
