"""API views to handle serialized data"""
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model

from core import models
from . import serializers


class UserViewset(viewsets.ModelViewSet):
    """User objects Viewset"""

    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # @action(detail=True, methods=['post'])
    # def set_password(self, request, pk=None):
    #     print('asdasd')
    #     user = self.get_object()
    #     serializer = serializers.UserPasswordChangeSerializer(
    #         data=request.data)
    #     print(serializer)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         print('bad request')
    #         return Response(serializer.errors,
    #                          status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewset(viewsets.ModelViewSet):
    """Profile objects Viewset"""

    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
