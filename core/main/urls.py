from django.urls import path
from .views import ItemAPIView

urlpatterns = [path("item-list", ItemAPIView.as_view(), name="item-list")]
