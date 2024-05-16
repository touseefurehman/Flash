from django.urls import path, include
from items import views


urlpatterns = [

path('pdp/<int:rental_item_id>', views.pdp, name='pdp'),

     

]


