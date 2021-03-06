from django.conf.urls import url
from django.contrib.auth import views as auth_views    

from . import views

urlpatterns = [
    url(r'^registration[/]*', views.registration, name='registration'),
    url(r'^about[/]*', views.about, name='about'),
    url(r'^home[/]*', views.home, name='home'), 
    url(r'^[/]*', views.index, name='index'),
]
