from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.services, name='Services'),

    #Services
    path('network design/', views.network_design, name='Network Design'),
    path('fiber optics services/', views.fiber_optics_services, name='Fiber Optics Services'),
    path('network management/', views.network_management, name='Network Management' ),
    path('osp insight/', views.osp_insight, name='OSP Insight' ),
    path('testing and terminations/', views.testing_and_terminations, name='Testing and Terminations' ),
    path('manhole placement/', views.manhole_placement, name='Manhole Placement' ),

]



