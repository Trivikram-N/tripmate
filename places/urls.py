from django.urls import path
from . import views

urlpatterns = [
    path('', views.places, name='places'),
    path("liked/", views.liked_places, name="liked"),

     path('like/<int:place_id>/', views.like_place, name='like_place'),
     path('details/<str:place_name>/', views.destination_details, name='destination-details'),
]
