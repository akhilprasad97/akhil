from django.conf.urls import url
from django.contrib import admin
from  . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^',views.log, name = 'logout'),
]
