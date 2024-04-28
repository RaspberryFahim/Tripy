from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
    path("places/", PlaceSearch.as_view(), name="place-search"),
    path("hotels/", HotelSearch.as_view(), name="hotel-search"),
    path("hotels/<int:pk>/", HotelDetail.as_view(), name="hotel-detail"),
    path("restaurants/", RestaurantSearch.as_view(), name="restaurant-search"),
    path("restaurants/<int:pk>/", ThingsToDoDetail.as_view(), name="restaurant-detail"),
    path("things-to-do/", ThingsToDoSearch.as_view(), name="things-to-do-search"),
    path("things-to-do/<int:pk>/", ThingsToDoDetail.as_view(), name="things-to-do-detail"),
]

