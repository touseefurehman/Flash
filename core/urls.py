from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.urls import path, include
from items import urls
from log import urls
from o import urls
from products import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('log.urls'), name='log'),
    path('items/',include('items.urls'),name='list_an_item'),
    path('', include('o.urls'), name='o'),
     path('accounts/', include('allauth.urls')),
    path('payment',include("products.urls"))

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
