from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/parking-data/', views.fetch_parking_data, name='fetch_parking_data'),
    path("recommend-worship-church/", views.recommend_worship_church, name="recommend_worship_church"),
    path("recommend-worship-mosque/", views.recommend_worship_mosque, name="recommend_worship_mosque"),
    path("recommend-shopping-places/", views.recommend_shopping_places, name="recommend_shopping_places"),
    path("recommend-tourist-sites/", views.recommend_tourist_sites, name="recommend_tourist_sites"),
    path("recommend-events/", views.recommend_events, name="recommend_events"),
    path("booking/", views.parking_page, name="booking"),
    path('book_parking_spot/<int:spot_id>/', views.book_parking_spot, name='book_parking_spot'),
]

