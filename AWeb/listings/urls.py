from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name = 'listings'),
    path('<int:listing_id>', views.listing, name = 'listing'),
    path('penus', views.penu_list , name= 'penu_list'),
    path('hydr', views.hydr_list , name= 'hydr_list'),
    path('valve', views.hydr_list , name= 'valve_list'),
  
]