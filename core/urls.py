from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from core import views as core_views
from items import urls
from account import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls'),name='account'),
    path('items/',include('items.urls'),name='list_an_item'),
    path('forget/', core_views.forget, name='forget'),
    path('reset/', core_views.pass_reset, name='reset'),
    path('home/', core_views.home, name='home'),
    path('rent/', core_views.rent, name='rent'),
    path('lend/', core_views.lend, name='lend'),
    path('profile/', core_views.profile, name='profile'),
    path('edit_profile/', core_views.edit_profile, name='edit_profile'),
    path('withdraw/', core_views.withdraw, name='withdraw'),
    path('inbox/', core_views.inbox, name='inbox'),
    path('search/', core_views.search, name='search'),  
    path('rental/', core_views.rental, name='rental'),  
    path('rental_list/', core_views.rental_list, name='rental_list'), 
    path('checkout/', core_views.checkout, name='checkout'),  
    path('my_item/', core_views.my_item, name='my_item'),  
    path('edit_item/', core_views.edit_item, name='edit_item'),      

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)