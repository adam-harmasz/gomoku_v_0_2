from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
import re

from gomoku_app.api.serializers import GomokuRecordSerializer
from core import models

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users objects"""
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        required=True,
        help_text='password needs to be at least 8 ',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    email = serializers.EmailField(validators=[UniqueValidator(
        queryset=User.objects.all(),
        message='That email address is already taken.'
    )])
    users_games = GomokuRecordSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'password', 'users_games')

    def create(self, validated_data):
        """create a new user with encrypted password and return it"""
        return User.objects.create_user(**validated_data)

    # def update(self, instance, validated_data):
    #     """Update a user, setting the password correctly and return it"""
    #     print(validated_data)
    #     password = validated_data.pop('password', None)
    #     user = super().update(instance, validated_data)
    #     print(user)
    #     if authenticate(username=user, password=password):
    #         return user
    #     raise serializers.ValidationError("Invalid password")

    # def validate(self, attrs):
    #     print(attrs)
    #     password = attrs['password']
    #     request = self.context.get('request')
    #     user = request.user
    #     print(user)
    #     user = authenticate(
    #         request=self.context.get('request'),
    #         username=user,
    #         password=password
    #     )
    #     if not user:
    #         raise serializers.ValidationError('Wrong password',
    #                                           code='authentication')
    #     return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for the profile objects"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'user', 'picture')
        read_only_fields = ('id',)

    def validate(self, attrs):
        """picture image validation"""
        allowed_formats = ('jpg', 'jpeg', 'gif')
        regex = r'([.]jpg$)|([.]jpeg$)|([.]gif$)'
        pic = str(attrs['picture'])
        pic_check = re.search(regex, pic)
        print(pic_check)
        if pic_check:
            return attrs
        raise serializers.ValidationError(
            'Invalid format of the file, allowed formats: jpg, jpeg, gif')


class UserProfilePictureSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to user profile"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'picture')
        read_only_fields = ('id',)


# class UserPasswordChangeSerializer(serializers.Serializer):
#     current_password = serializers.CharField(
#         label='Current password',
#         style={'input_type': 'password', 'placeholder': 'Password'})
#     new_password = serializers.CharField(
#         label='New password',
#         style={'input_type': 'password', 'placeholder': 'Password'})
#     re_new_password = serializers.CharField(
#         label='New password',
#         style={'input_type': 'password', 'placeholder': 'Password'})
