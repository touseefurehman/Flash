from django.urls import path, include
from items import views

from items import views

urlpatterns = [
path('list_an_item/',views.rental_item_form,name='list_an_item'),    
path('search_by_category/',views.test, name="search_by_category"),
    path('pdp', views.pdp, name='pdp'),

]


