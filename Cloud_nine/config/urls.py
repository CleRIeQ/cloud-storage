from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls')),
    #path('auth/', include('djoser.urls.jwt')),
    #path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.authtoken')),
    path('user/', include('profiles.urls')),
    path('user/files/', include('users_files.urls')),
]
