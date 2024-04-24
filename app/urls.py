from django.urls import path
from app import views

urlpatterns = [
    path('1/', views.home1),
    path('2/', views.camera),
    path('3/', views.pdp),
    path('4/', views.checkout),
    path('5/', views.rental),
    path('6/', views.rental_list),
    path('7/', views.profile),
    path('signin/', views.sign),
    
]
