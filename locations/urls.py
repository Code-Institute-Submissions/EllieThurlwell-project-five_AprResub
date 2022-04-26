from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_locations, name='locations'),
    path('add/', views.add_location, name='add_location'),
    path('edit/<int:location_id>/', views.edit_location, name='edit_location'),
]
