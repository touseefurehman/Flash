
from django.contrib import admin
from django.urls import path, include
from . import views
from items import urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', views.signin, name='login'), 
    path('signup/',views.signup, name='signup'),
    path('setupprofile/',views.bio2, name='setupprofile'),
    path('profile/', views.profile, name='profile'),
    path("user_logout/", views.user_logout, name="user_logout")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)