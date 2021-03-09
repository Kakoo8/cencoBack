import json
import redis
import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from time import time, sleep
import random
import datetime
# Redis instance
loaded=False
redis = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT, db=0)

@api_view(['GET'])
def manage_items(request, *args, **kwargs):
    if request.method == 'GET':
        items = {}
        count = 0
        for key in redis.keys("*"):
            items[key.decode("utf-8")] = redis.get(key)
            count += 1
        response = {
           'items': items
        }
        return Response(response, status=200)
    

@api_view(['GET'])
def manage_item(request, *args, **kwargs):
    if request.method == 'GET':
        if kwargs['key']:
            value = redis.get(kwargs['key'])
            if value:
                response = {
                    'key': kwargs['key'],
                    'value': value,
                    'msg': 'success'
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)

   
@api_view(['GET','POST'])
def set_error(request, *args, **kwargs):
    if request.method == 'POST':
        item = json.loads(request.body)
        key = list(item.keys())[0]
        value = item[key]
        redis.set(key, value)
        response = {
            'msg': "'How unfortunate! The API RequestFailed'"
         }
    return Response(response, 201)


@api_view(['GET'])
def get_byCity(params):
    city="Londres"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=5757b7e8a314027da52fac9129369161" 
    response = generate_request(url, params)
    if response:

        coord  = response.get("coord")
        lat= coord['lat']
        lon= coord['lon']
        key1= city +"Lat"
        key2= city + "Lon"
        redis.set(key1, lat)
        redis.set(key2, lon)   
        return Response(key1, status=status.HTTP_200_OK)

    return Response("Error", status=500)




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



 
    

@api_view(['GET'])
def get_weather(request, *args, **kwargs):
    
    if kwargs['key']:

        lat = json.loads(redis.get(kwargs['key'] + 'Lat'))
        
        lon = json.loads(redis.get(kwargs['key'] + 'Lon'))
        
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=c373cc5c75cb95bd584db9668289be86"
       
        
        return Response(get_dataW(url, kwargs['key'], args), status=status.HTTP_200_OK)


def get_dataW(url, city, args):
        time=datetime.datetime.now()
        if (random.uniform(0, 1) < 0.1):

            redis.set(time.timestamp(), "error Consulting "+city)
            get_dataW(url,city,args)
            
            
        else:
            redis.set(time.timestamp(), "error Consulting "+city)
            response = generate_request(url, args)
            if response:
                return response
    

    

if(loaded==False):
    get_allCities("")
    loaded=True

      
        

