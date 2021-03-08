from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    path('items', manage_items, name="items"),
    path('<slug:key>', manage_item, name="single_item"),
    path('clima/London', get_byCity, name="byCity"),
    path('weather/<slug:key>', get_weather, name="weather"),
    path('coord/cities', get_allCities, name="cities"),
    path('error', set_error, name="error")
}
urlpatterns = format_suffix_patterns(urlpatterns)
