from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from core import models

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users objects"""
    password = serializers.CharField(
        write_only=True,
        min_length=5,
        required=True,
        help_text='password needs to be at least 5 ',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """create a new user with encrypted password and return it"""
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user

