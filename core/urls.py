from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.urls import path, include
from items import urls
from account import urls
from o import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls'), name='account'),
    path('items/',include('items.urls'),name='list_an_item'),
    path('o/', include('o.urls'), name='o'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)