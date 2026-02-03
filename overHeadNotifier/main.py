import requests
import datetime

my_lat = 33
my_lng = 23

parametrs = {
    "lat" : my_lat
    "lng" : my_lng
}

respond = requests.get(url=)
respond.raise_for_status()
data = respond.json
