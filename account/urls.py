
from django.contrib import admin
from django.urls import path, include
from . import views
from items import urls
urlpatterns = [

    path('', views.signin, name='signin'), 

    path('signup/',views.signup, name='signup'),
]