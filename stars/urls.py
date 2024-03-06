from django.urls import path
from . import views

urlpatterns = [
    path('stars/', views.star, name = 'star'),
    path('about/', views.about, name = "about"),
    path('/', views.home, name= "home")

]