#data_collection.py                                          
import requests
import random

def fetch_weather_data(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed']
    }

def simulate_sensor_data():
    return {
        'no2_sensor': round(random.uniform(10, 100), 2)
    }

def get_combined_data(api_key, lat, lon):
    weather = fetch_weather_data(api_key, lat, lon)
    sensor = simulate_sensor_data()
    return {**weather, **sensor}