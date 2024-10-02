from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.contrib.auth import authenticate
from .models import User, Item
from .serializers import (
    UserSerializers,
    UserProfileSerializers,
    ActionSerializers,
    ActionLogSerializers,
    ItemSerializer,
)


# Item API view for authenticated users
class ItemAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


# User Registration View
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.AllowAny]  # Allow any user to register

    def create(self, request, *args, **kwargs):
        # Call the super method to create the user
        response = super().create(request, *args, **kwargs)

        # Get the user instance by using the username or phone number from request
        user = User.objects.get(
            phone_number=response.data["phone_number"]
        )  # Assuming phone_number is unique

        # Create token for the user
        token, created = Token.objects.get_or_create(user=user)

        # Append the token to the response data
        response.data["token"] = token.key
        return response


# User Login View
class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Use the ObtainAuthToken's method to validate credentials
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the user object
        user = serializer.validated_data["user"]

        # Create or get the token
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})


# User List and Retrieve, Update, Destroy Views
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]  # Ensure authenticated access
