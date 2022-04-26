from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin_controls/', views.admin_controls, name='admin_controls'),
]
