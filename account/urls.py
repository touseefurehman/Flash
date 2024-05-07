
from django.contrib import admin
from django.urls import path, include
from . import views
from .models import bio
from items import urls
urlpatterns = [

    path('', views.signin, name='signin'), 

    path('signup/',views.signup, name='signup'),
    path('setupprofile/',views.bio, name='setupprofile'),

]