from django.http import HttpResponse
from django.shortcuts import render
from .models import UserProfile, UserFile
from .forms import UploadFileForm
from django.views.generic import View
from config.settings import MEDIA_ROOT
import mimetypes

class UserData(View):
    model = UserProfile
    template_name = 'account/dashboard.html'
    context_object_name = 'user'
    form_class = UploadFileForm
    

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.form_class()
            all_files = UserFile.objects.filter(user_id=request.user.id) 
            return render(request, self.template_name, {'form': form, 'files': all_files})
        else:
            return HttpResponse("login needed")
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
        return render(request, self.template_name, {'form': form})
        

class DownloadFile(View):
    model = UserProfile
    template_name = "file/download.html"
    context_opbject_name = "file"
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            file = UserFile.objects.filter(user_id=request.user.id) 
            return render(request, self.template_name, {'file': file})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            username = request.user.username
            filename = request.POST.get('filename')
            filepath = MEDIA_ROOT + f"\\{filename}"
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)
            #filename = filename.split("/")
            #file_name = filename[3]
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
 

    
