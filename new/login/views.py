from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import Login

def get_credentials(request) :
    if request.method == 'POST' :
        form = Login(request.POST)
        if form.is_valid() :
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username = username, password = password)
            if user is not None :
                login(request, user)
                return HttpResponseRedirect('/profile')
                #return HttpResponseRedirect('/profile')
            else :
                return HttpResponseRedirect('')
    else :
        form = Login()
    return render(request, 'login/login.html', {'form' : form})

# Create your views here.
