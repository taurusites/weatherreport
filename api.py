import requests


apikey = "5b420cc97b3e8854d34ef3f969298896"  # API key
url = f'https://api.openweathermap.org/data/2.5/weather?appid=' + f'{apikey}'

def weather_api_lookup(list_of_cities):
  city_weather_data = {'City':'','Weather':{}};
  for city in list_of_cities:
    city_weather_data.update({f"{city}":f"{requests.get(url + f'&q={city}').json()}"})
  return city_weather_data
    