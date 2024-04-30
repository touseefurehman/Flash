from django.urls import path
from app import views

urlpatterns = [

    
  
    path('4/', views.checkout),

    
    path('signin/', views.sign),
    
]
