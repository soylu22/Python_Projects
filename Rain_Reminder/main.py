# api_key = "a3c1aada85c0afc35ef71ea851b1f623"

import requests

OWM = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "a3c1aada85c0afc35ef71ea851b1f623"

weather_params = {
    "appid": api_key,
    "lat": 9.0192,
    "lon": 38.7525,
    "appid": api_key,
    "exclude": "currrent, minutely, daily"
}

response = requests.get(OWM, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)


