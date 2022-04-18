from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import ProfileSerializer

class UserData(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
