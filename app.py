import inputs
import api
import data_processing
import output

def app():
  list_of_cities = inputs.inputs()
  api.api_lookup(list_of_cities)

if __name__ == "__main__":
  app()