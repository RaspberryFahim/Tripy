from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.serializers import *


class PlaceFilter(filters.FilterSet):
    country = filters.CharFilter(field_name="country", lookup_expr='icontains')
    state = filters.CharFilter(field_name="state", lookup_expr='icontains')
    city = filters.CharFilter(field_name="city", lookup_expr='icontains')

    class Meta:
        model = Place
        fields = ['country', 'state', 'city']


class PlaceSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlaceFilter


class HotelFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    address = filters.CharFilter(field_name="address", lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_rating = filters.NumberFilter(field_name="average_rating", lookup_expr='gte')

    class Meta:
        model = Hotel
        fields = [
            'name',
            'place',
            'address',
            'allows_free_cancellation',
            'allows_pay_at_stay',
            'allows_special_offers',
            'has_free_wifi',
            'has_free_parking',
            'has_restaurant',
            'has_pool',
            'has_ac',
            'min_price',
            'max_price',
            'min_rating'
        ]


class HotelSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HotelFilter


class HotelDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class RestaurantFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    price = filters.CharFilter(field_name="price", lookup_expr='icontains')
    address = filters.CharFilter(field_name="address", lookup_expr='icontains')
    min_rating = filters.NumberFilter(field_name="average_rating", lookup_expr='gte')

    class Meta:
        model = Restaurant
        fields = [
            'name',
            'place',
            'address',
            'allows_free_cancellation',
            'allows_special_offers',
            'has_free_wifi',
            'has_free_parking',
            'price',
            'min_rating',
            'has_bengali',
            'has_international',
            'has_indian',
            'has_thai',
            'has_chinese',
            'has_mexican',
            'has_italian',
            'has_korean',
            'has_bar',
            'has_fast_food',
        ]


class RestaurantSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RestaurantFilter


class RestaurantDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class ThingsToDoFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = ThingsToDo
        fields = ['name', 'place']


class ThingsToDoSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ThingsToDoSerializer
    queryset = ThingsToDo.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ThingsToDoFilter


class ThingsToDoDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ThingsToDoSerializer
    queryset = ThingsToDo.objects.all()
