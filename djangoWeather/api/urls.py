
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import re_path

urlpatterns = {
   
    path('weather/cities', get_weather, name="weather"),
    path('coord/cities', get_allCities, name="cities"),
    
}




urlpatterns = format_suffix_patterns(urlpatterns)
