from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views 
from items import urls
from account import urls
urlpatterns = [
    path('forget/', views.forget, name='forget'),
    path('reset/', views.pass_reset, name='reset'),
    path('', views.home, name='home'),
    path('rent/', views.rent, name='rent'),
    path('lend/', views.lend, name='lend'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('inbox/', views.inbox, name='inbox'),
    path('search/', views.search, name='search'),  
    path('rental/', views.rental, name='rental'),  
    path('rental_list/', views.rental_list, name='rental_list'), 
    path('checkout/', views.checkout, name='checkout'),  
    path('my_item/', views.my_item, name='my_item'),  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)