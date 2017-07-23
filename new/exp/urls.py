from django.conf.urls import url
from django.contrib import admin
from  . import views
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^',TemplateView.as_view(template_name = 'saved.html')),
    url(r'^',views.profile, name = 'profile'),
    #url(r'^(\d+)/(\d+)$',views.profile, name = 'profile'),

]
