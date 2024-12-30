from django.urls import path 
from . import views



urlpatterns = [

    path('', views.contact, name='contact'),
    path('ajax/subscribe/', views.subscribe, name='ajax_subscribe'),   
]