
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', views.signin, name='signin'),
    path('forget/', views.forget, name='forget'),
    path('reset/', views.pass_reset, name='reset'),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('rent/', views.rent, name='rent'),
    path('lend/', views.lend, name='lend'),
    path('list_an_item/', views.list_an_item, name='listlend'),
    path('search_by_category/', views.camera, name='search_by_category'),
    path('pdp/', views.pdp, name='pdp'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('inbox/', views.inbox, name='inbox'),
    path('search/', views.search, name='search'),  
    path('rental/', views.rental, name='rental'),  
    path('rental_list/', views.rental_list, name='rental_list'), 
    path('checkout/', views.checkout, name='checkout'),  
    path('my_item/', views.my_item, name='my_item'),  
    path('edit_item/', views.edit_item, name='edit_item'),  
]
