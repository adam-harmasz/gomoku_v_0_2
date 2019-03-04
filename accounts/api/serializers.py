from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

from core import models

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users objects"""
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        required=True,
        help_text='password needs to be at least 5 ',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    email = serializers.EmailField(validators=[UniqueValidator(
        queryset=User.objects.all(),
        message='That email address is already taken.'
    )])

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'password')
        # extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
        # validators = [UniqueTogetherValidator(
        #     queryset=User.objects.all(),
        #     fields='email',
        #     message='Such email already exists'
        # )]

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


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for the profile objects"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'user', 'picture')
        read_only_fields = ('id',)


class UserProfilePictureSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to user profile"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'picture')
        read_only_fields = ('id',)
