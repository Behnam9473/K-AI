from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name = 'news'),  
    path('news/<int:news_id>', views.new, name = 'new'),

]