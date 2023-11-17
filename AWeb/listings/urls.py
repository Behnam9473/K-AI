from django.urls import path
from . import views

urlpatterns = [
    
    path('hydros', views.hydro_listings, name = 'hydro_listings'),
    path('hydros/<int:listing_id>', views.hydro_listing, name = 'hydro_listing'),

    path('penues', views.penu_listings, name = 'penu_listings'),
    path('penues/<int:listing_id>', views.penu_listing, name = 'penu_listing'),

    # path('penus', views.penu_list , name= 'penu_list'),
    # path('hydr', views.hydr_list , name= 'hydr_list'),
    # path('valve', views.hydr_list , name= 'valve_list'),
  
]