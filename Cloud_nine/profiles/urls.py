from django.contrib import admin
from .views import UserData
from django.urls import URLPattern, path, include, re_path

urlpatterns = [
    path('<int:pk>/profile/', UserData.as_view())
]