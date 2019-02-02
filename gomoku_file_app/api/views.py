from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.mixins import CreateModelMixin, ListModelMixin

from django.contrib.auth import get_user_model

from core import models
from . import serializers

User = get_user_model()


class GomokuRecordImageViewset(viewsets.ModelViewSet):
    """Viewset to handle uploading file with game record"""
    serializer_class = serializers.GomokuRecordFileSerializer
    queryset = models.GomokuRecordFile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload a game record file"""
        gomoku_record = self.get_object()
        serializer = self.get_serializer(
            gomoku_record,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
