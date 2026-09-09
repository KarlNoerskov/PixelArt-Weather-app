import pygame

from rendering.raindrop import Raindrop
from weather_data.weather_data_api import WeatherData

BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
WIDTH = 800
HEIGHT = 800

pygame.init()
pygame.display.set_caption("PixelArt Weather Simulator")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 1. Hent vejrdata én gang
weather_man = WeatherData()
weather_data = weather_man.get_weather_data()
#wind = weather_data['wind_speed_10m']
#is_raining = weather_data['precipitation'] > 0

raindropPic = pygame.image.load('assets/rain.png')
raindropImage = pygame.transform.smoothscale(raindropPic,(50,60))
raindropRect = raindropImage.get_rect()


#fake data
is_raining = True
wind = 5.0


raindrops = []
raindrop_effect_particles = []


while True:
    screen.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if is_raining:
        raindrops.append(Raindrop(WIDTH, wind, raindropImage))

    for rain in raindrops:
            rain.draw(screen)
            rain.fall(screen, raindrop_effect_particles)

    for particle in raindrop_effect_particles:
        particle.update()
        particle.draw(screen)

    raindrops = [rain for rain in raindrops if rain.y < HEIGHT]
    raindrop_effect_particles = [p for p in raindrop_effect_particles if p.timer > 0]


    pygame.display.flip()
    clock.tick(30)
