from django import forms
from .models import UserFile, UserProfile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file']
