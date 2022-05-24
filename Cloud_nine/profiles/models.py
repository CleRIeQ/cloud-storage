from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    return 'files/user/{0}/{1}'.format(instance.user.username, filename)
    

class UserProfile(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    
class UserFile(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    file = models.FileField(upload_to=user_directory_path, blank=True, null=True)

