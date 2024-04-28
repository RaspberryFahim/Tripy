from django.db import models
from datetime import datetime


def upload_to(instance, name):
    return f"images/{int(datetime.now().timestamp())}_{name}"


class Place(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # Image
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    display_image_1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    display_image_2 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    display_image_3 = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    # Deals
    allows_free_cancellation = models.BooleanField(blank=True, default=False)
    allows_pay_at_stay = models.BooleanField(blank=True, default=False)
    allows_special_offers = models.BooleanField(blank=True, default=False)
    # Amenities
    has_free_wifi = models.BooleanField(blank=True, default=False)
    has_free_parking = models.BooleanField(blank=True, default=False)
    has_restaurant = models.BooleanField(blank=True, default=False)
    has_pool = models.BooleanField(blank=True, default=False)
    has_ac = models.BooleanField(blank=True, default=False)
    # Prices
    price = models.FloatField()
    # Ratings
    total_ratings = models.PositiveIntegerField(blank=True, default=0)
    average_rating = models.FloatField(blank=True, default=0.0)
    # Image
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # Hotel Site
    link = models.URLField(blank=True, null=True)
    # Contact Info
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=63, blank=True, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=63)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    is_vacant = models.BooleanField(blank=True, default=True)
    booked = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.hotel.name} | {self.number}"


class Restaurant(models.Model):
    PRICE_OPTIONS = [
        ('low', 'Low'),
        ('mid', 'Mid'),
        ('high', 'High'),
    ]
    name = models.CharField(max_length=255)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    # Deals
    allows_free_cancellation = models.BooleanField(blank=True, default=False)
    allows_special_offers = models.BooleanField(blank=True, default=False)
    # Amenities
    has_free_wifi = models.BooleanField(blank=True, default=False)
    has_free_parking = models.BooleanField(blank=True, default=False)
    # Prices
    price = models.CharField(max_length=7, choices=PRICE_OPTIONS, blank=True, default='low')
    # Ratings
    total_ratings = models.PositiveIntegerField(blank=True, default=0)
    average_rating = models.FloatField(blank=True, default=0.0)
    # Image
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    display_image_1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    display_image_2 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    display_image_3 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # Restaurant Site
    link = models.URLField(blank=True, null=True)
    # Contact Info
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=63, blank=True, null=True)
    # Cuisines
    has_bengali = models.BooleanField(blank=True, default=False)
    has_international = models.BooleanField(blank=True, default=False)
    has_indian = models.BooleanField(blank=True, default=False)
    has_thai = models.BooleanField(blank=True, default=False)
    has_chinese = models.BooleanField(blank=True, default=False)
    has_mexican = models.BooleanField(blank=True, default=False)
    has_italian = models.BooleanField(blank=True, default=False)
    has_korean = models.BooleanField(blank=True, default=False)
    has_bar = models.BooleanField(blank=True, default=False)
    has_fast_food = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.name


class RestaurantMenu(models.Model):
    FOOD_CATEGORY = [
        ('general', 'General'),
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('desert', 'Desert'),
        ('drink', 'Drink'),
    ]

    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    category = models.CharField(max_length=31, choices=FOOD_CATEGORY, default='general')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.restaurant} | {self.name}'


class ThingsToDo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    display_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} | {self.place}'
