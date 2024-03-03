from django.urls import path
from . import views

urlpatterns = [
    path('stars/', views.star, name = 'star'),

]