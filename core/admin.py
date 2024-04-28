from django.contrib import admin

from core.models import *


class CustomAdminConfig(admin.ModelAdmin):
    list_display = ['id', 'name', 'place']
    list_select_related = ['place']
    list_filter = ['name', 'place']


admin.site.register(Place)
admin.site.register(Hotel, admin_class=CustomAdminConfig)
admin.site.register(Room)
admin.site.register(Restaurant, admin_class=CustomAdminConfig)
admin.site.register(RestaurantMenu)
admin.site.register(ThingsToDo, admin_class=CustomAdminConfig)
