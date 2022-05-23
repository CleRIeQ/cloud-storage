from .views import UserData, DownloadFile
from django.urls import path, include

urlpatterns = [
    path('<int:pk>/profile/', UserData.as_view()),
    path('', include('allauth.urls')),
    path('download/', DownloadFile.as_view(), name="download")
    
]