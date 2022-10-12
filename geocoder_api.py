import geocoder
import requests

API_KEY = 'xxxxxxxxx'

API_BASE_URL = f'https://api.openweathermap.org/data/2.5/weather?units=imperial&appid={API_KEY}'

def lat_long(destination):
  location = geocoder.arcgis(destination)
  response = location.latlng
  for item in response:
    if item == response[0]:
      latitude = float(item)
      response[0] == round(latitude, 2)
    elif item == response[1]:
      longitude = float(item)
      response[1] == round(longitude, 2)
    print(f'{destination} is located at ({response[0]:.4f},{response[1]:.4f})')
    return response
      

def weather(destination, coordinates):
  lat = coordinates[0]
  lon = coordinates[1]
  full_api_url = f'{API_BASE_URL}&lat={lat}&lon={lon}'
  result = requests.get(full_api_url).json()
  print(f"At {destination} right now, it's {result['weather'][0]['description']} with a temperature of {result['main']['temp']}")

def main():
  destinations = [
  'Space Needle',
  'Crater Lake',
  'Golden Gate Bridge',
  'Yosemite National Park',
  'Las Vegas, Nevada',
  'Grand Canyon National Park',
  'Aspen, Colorado',
  'Mount Rushmore',
  'Yellowstone National Park',
  'Sandpoint, Idaho',
  'Banff National Park',
  'Capilano Suspension Bridge']

 
  for destination in destinations:
    coordinates = lat_long(destination)
    weather(destination, coordinates)
   
main()
