import requests

class WeatherData:
    def __init__(self):
        pass
    
    def get_weather_data(self):
        url = "https://api.open-meteo.com/v1/forecast?latitude=55.6761&longitude=12.5683&current=temperature_2m,precipitation,wind_speed_10m,cloud_cover&daily=sunrise,sunset&timezone=Europe%2FCopenhagen"
        
        response = requests.get(url)
        data = response.json()
        
        current = data["current"]
        daily = data["daily"]
        
        print(f"Temp: {current['temperature_2m']}°C")
        print(f"Rain: {current['precipitation']} mm")
        print(f"Wind: {current['wind_speed_10m']} km/t")
        print(f"Clouds: {current['cloud_cover']} %")
        print(f"Sunrise: {daily['sunrise'][0]}")
        print(f"Sunset: {daily['sunset'][0]}")
        
        return current, daily