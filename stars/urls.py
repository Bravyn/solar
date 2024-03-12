from django.urls import path
from . import views

urlpatterns = [
    path('', views.star, name = "star"),
    path('home/about/', views.about, name = "about"),
    path('stars/home/', views.home, name= "home")

]