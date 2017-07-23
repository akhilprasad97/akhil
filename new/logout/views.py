from django.shortcuts import render
from django.contrib.auth import logout

def log(request) :
    logout(request)
    return render(request, template_name='logout/success.html')

# Create your views here.
