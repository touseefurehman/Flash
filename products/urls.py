from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views 
from items import urls
from log import urls
urlpatterns = [
path('withdraw/', views.withdraw, name='withdraw'),
path("success/", views.success, name="success"),
path("cancel/", views.cancel, name="cancel"),

]




