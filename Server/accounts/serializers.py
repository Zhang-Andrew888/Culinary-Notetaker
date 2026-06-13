from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from .models import UserProfile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["created_at", "updated_at"]
        read_only_fields = fields


class UserReadSerializer(serializers.ModelSerializer):
    """
    Get User Profile.
    """
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "profile"]
        read_only_fields = fields


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Update User Profile.
    """
    class Meta:
        model = User
        fields = ["username"]


class RegisterSerializer(serializers.ModelSerializer):
    """
    Create a new user. Requires a username and password.
    """
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs["username"],
            password=attrs["password"],
        )

        if user is None:
            raise serializers.ValidationError("Invalid username or password.")
        if not user.is_active:
            raise serializers.ValidationError("This account is disabled.")
        
        attrs["user"] = user
        return attrs
