from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Upload
from .models import XML, Image
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def profile(request) :
    saved = False
    img = Image.objects.get(title='1')
    for i in Image.objects.all() :
        if i.verify is False :
            img = i
            i.save()
            break
    a = img.title
    if request.method == "POST" :
        form = Upload(request.POST, request.FILES)
        if form.is_valid() :
            file = XML()
            file.title = a
            file.image = img
            file.xml = form.cleaned_data["file"]
            file.save()
            saved = True
            i.verify=True
            i.save()
    else :
            form = Upload()
    return render(request, 'experiment/upload.html', {'form' : form, 'image' : img})
        
            

# Create your views here.
