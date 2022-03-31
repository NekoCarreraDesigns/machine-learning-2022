from wsgiref.util import request_uri
import requests

API_KEY = 'a8873d0d448c9dc93f60cba6ef75cb3e'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('enter a city name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    print('weather:', weather)
    print('temperature:', temperature, 'celsius')
else:
    print('error')
