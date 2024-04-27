from django.urls import path
from app import views

urlpatterns = [
    path('1/', views.home1),
    
  
    path('4/', views.checkout),
    path('5/', views.rental),
    path('6/', views.rental_list),
    
    path('signin/', views.sign),
    
]
