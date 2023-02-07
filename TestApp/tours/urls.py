from django.urls import path
from . import views
urlpatterns = [
    path('', views.tours_home, name= 'home_tours'),
]