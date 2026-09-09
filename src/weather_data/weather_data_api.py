import requests


class WeatherData:
    def __init__(self):
        pass
    
    def get_weather_data(self):
        url = "https://api.open-meteo.com/v1/forecast?latitude=55.6761&longitude=12.5683&current=temperature_2m,precipitation,wind_speed_10m"
        
        response = requests.get(url)
        data = response.json()
        
        current = data["current"]
        print(f"Temperatur: {current['temperature_2m']}°C")
        print(f"Regn: {current['precipitation']} mm")
        print(f"Vind: {current['wind_speed_10m']} km/t")
        
        return current
