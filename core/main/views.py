from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

# Core imports
from .models import Item
from .serializers import ItemSerializer


# Create your views here.
class ItemAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
