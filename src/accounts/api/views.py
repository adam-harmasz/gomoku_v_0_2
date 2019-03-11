from rest_framework import viewsets

from django.contrib.auth import get_user_model
from rest_framework import permissions

from core import models
from . import serializers

User = get_user_model()


class UserViewset(viewsets.ModelViewSet):
    """User objects Viewset"""

    queryset = User.objects.all()
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
