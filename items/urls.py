from django.urls import path, include
from items import views


urlpatterns = [
path('list_an_item/',views.rental_item_form,name='list_an_item'),    
path('search_by_category/',views.test, name="search_by_category"),
path('search_by_list/',views.test, name="search_by_list"),
path('pdp/<int:rental_item_id>', views.pdp, name='pdp'),
path('edit_item/<int:item_id>', views.edit_item, name='edit_item'),      
path('my_item/', views.my_item, name='my_item'), 
     

]


