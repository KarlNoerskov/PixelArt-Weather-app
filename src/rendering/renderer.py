import pygame
import random


from rendering.raindrop import Raindrop
from rendering.tree import Tree
from rendering.wind import Wind
from rendering.cloud import Cloud
from rendering.sun import Sun
from rendering.star import Star
from rendering.asset_manager import AssetManager

class Renderer:
    def __init__(self, width, height, rain_today, wind, cloudy, is_raining, Sunsettime, Sunrisetime, datetime):
        self.WIDTH = width
        self.HEIGHT = height
        self.rainToday = rain_today
        self.wind = wind
        self.cloudy = cloudy
        self.is_raining = is_raining

        self.sunset_time = Sunsettime
        self.sunrise_time = Sunrisetime

        self.time = datetime
        self.time_in_minutes = self.time.hour * 60 + self.time.minute

        self.time_since_midnight_sunrise = int(self.sunrise_time.split(":")[0]) * 60 + int(self.sunrise_time.split(":")[1])
        self.time_since_midnight_sunset = int(self.sunset_time.split(":")[0]) * 60 + int(self.sunset_time.split(":")[1])


        self.is_day = self.time_in_minutes >= self.time_since_midnight_sunrise and self.time_in_minutes <= self.time_since_midnight_sunset
        self.night = not self.is_day

        self.NIGHT = (49, 47, 54)
        self.BLUE = (135, 206, 235)
        self.CLOUDYBLUE = (172, 194, 217)
        if self.night: 
            self.screen_color = self.NIGHT
        elif self.cloudy > 50:
            self.screen_color = self.CLOUDYBLUE
        else:
            self.screen_color = self.BLUE

        self.asset_manager = AssetManager()

        raindropPic = self.asset_manager.get_image("rain")
        self.raindropImage = pygame.transform.smoothscale(raindropPic, (10, 15))


        if not self.night:
            self.sun = Sun(self.sunrise_time, self.sunset_time, datetime,  self.WIDTH, self.HEIGHT)

        self.clouds = [Cloud(self.WIDTH, self.HEIGHT, self.asset_manager.get_cloud()) for _ in range(self.cloudy)]

        self.winds = [Wind(self.wind, self.WIDTH, self.HEIGHT, self.asset_manager.file_dictionary["Wind"]) for _ in range(round(self.wind * 1.5))]

        self.trees = []
        AmountofTrees = 15
        scaleOfTrees = 400
        zone_width = self.WIDTH // AmountofTrees

        for i in range(AmountofTrees):
            zone_start = i * zone_width
            zone_end = zone_start + zone_width
            x_pos = random.randrange(zone_start, zone_end)
            y_pos = self.HEIGHT
            scale = scaleOfTrees - random.randrange(0, 200)
            self.trees.append(Tree(x_pos, y_pos, scale, self.wind, self.asset_manager.file_dictionary))

        self.raindrops = []
        self.raindrop_effect_particles = []

        if self.night:
            self.stars_amount = 30
            self.stars = [Star(random.randrange(0, self.WIDTH), random.randrange(0, self.HEIGHT // 2), self.asset_manager.get_star()) for _ in range(self.stars_amount)]


    def update(self, screen):
        screen.fill(self.screen_color)
        if not self.night:
            self.sun.update(screen)


        for star in self.stars:
                    star.update(screen)


        if self.is_raining:
            for rain in range(self.rainToday * 2):
                self.raindrops.append(Raindrop(self.WIDTH, self.wind, self.raindropImage))

        for tree in self.trees:
            tree.update(screen)

        for rain in self.raindrops:
            rain.update(self.raindrop_effect_particles, screen)

        for x in self.winds:
            x.update(screen)

        for particle in self.raindrop_effect_particles:
            particle.update()
            particle.draw(screen)

        if self.night:
            for cloud in self.clouds:
                cloud.update(screen)


        self.raindrops = [rain for rain in self.raindrops if rain.y < self.HEIGHT]
        self.raindrop_effect_particles = [p for p in self.raindrop_effect_particles if p.timer > 0]