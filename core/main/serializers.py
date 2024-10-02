# serializers.py
from rest_framework import serializers
from .models import User, UserProfile, Action, ActionLog, Item


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "phone_number", "date_of_birth", "bio"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Ensure the password is hashed during user creation
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "user", "location", "avatar"]


class ActionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "title"]


class ActionLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActionLog
        fields = ["id", "user", "action", "created_at"]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "title", "description"]
