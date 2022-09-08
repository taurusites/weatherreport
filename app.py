import inputs
import api
import data_processing
import output

def app():
  list_of_cities = inputs.inputs()
  city_weather_data = api.weather_api_lookup(list_of_cities)
  print(city_weather_data)
if __name__ == "__main__":
  app()