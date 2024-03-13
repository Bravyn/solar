from django.urls import path
from . import views

urlpatterns = [
    path('', views.star, name = "star"),
    path('home/about/', views.about, name = "about"),
    path('stars/', views.home, name= "home"),
    path('stars/star_details/', views.star_details, name= "star_details")

]