import pygame
import datetime

from weather_data.weather_data_api import WeatherData
from rendering.renderer import Renderer


WIDTH = 800
HEIGHT = 800

pygame.init()
pygame.display.set_caption("PixelArt Weather Simulator")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

weather_man = WeatherData()
current_data, daily_data = weather_man.get_weather_data()
time = datetime.datetime.now()

is_raining = current_data['precipitation'] > 0.0
rainToday = current_data['precipitation'] 
wind = current_data['wind_speed_10m'] / 3.6
cloudy = current_data['cloud_cover']

cloudy = current_data['cloud_cover']
sunrise_time = daily_data['sunrise'][0].split('T')[1]
sunset_time = daily_data['sunset'][0].split('T')[1]

# Fake data
#is_raining = True
#rainToday = 10 #mm
#wind = 6 #m/s
#cloudy = 50
#sunrise_time = "06:00"
#sunset_time = "20:00"
#time = datetime.datetime(2026, 9, 11, 20, 30)

renderer = Renderer(WIDTH, HEIGHT, rainToday, wind, cloudy, is_raining, sunset_time, sunrise_time, time)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    renderer.update(screen)

    pygame.display.flip()
    clock.tick(30)