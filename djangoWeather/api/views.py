
import time
import schedule
import json
import redis
import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from asgiref.sync import async_to_sync
from time import time, sleep
import random
import datetime
# Redis instance
loaded=False
redis = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT, db=0)








def get_allCities(params):
    cities={'London','Santiago','Zurich','Auckland','Sydney','Georgia'}
    for city in cities:
        get_City(city,params)

    return Response("Saved",status=status.HTTP_200_OK)


def get_City(city,params):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c373cc5c75cb95bd584db9668289be86"
    response = generate_request(url, params)
    if response:

        coord  = response.get("coord")
        lat= coord['lat']
        lon= coord['lon']
        key1= city +"Lat"
        key2= city + "Lon"
        redis.set(key1, lat)
        redis.set(key2, lon)   
        return Response("OK", status=status.HTTP_200_OK)

    return Response("Error", status=500)

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()



 
    


def get_weather(params):
    
    cities = ['London', 'Santiago', 'Zurich', 'Auckland', 'Sydney', 'Georgia']
    data=[]
    
    for city in cities: 

        lat = json.loads(redis.get(city + 'Lat'))
        
        lon = json.loads(redis.get(city + 'Lon'))
        
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=c373cc5c75cb95bd584db9668289be86"
        data.append(get_dataW(url, city, params))
        
    return data


def get_dataW(url, city, args):
        time=datetime.datetime.now()
        if (random.uniform(0, 1) < 0.1):

            redis.set(time.timestamp(), "error Consulting "+city)
            get_dataW(url,city,args)
            
            
        else:
            
            response = generate_request(url, args)
            if response:
                return response
    

    

if(loaded==False):
    get_allCities("")
    loaded=True



      
        

