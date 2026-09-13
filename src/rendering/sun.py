import pygame
import datetime
import math

class Sun:
    def __init__(self, Sunrisetime, Sunsettime, Time, WIDTH, HEIGHT):
        self.sunrise_time = Sunrisetime
        self.sunset_time = Sunsettime
        self.sun_positions = 20
        self.radius = 100
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.horizon = HEIGHT/2
        self.arc_height = self.horizon

        self.time_of_day = Time

        h_since_midnight_sunrise = int(self.sunrise_time.split(":")[0]) * 60 + int(self.sunrise_time.split(":")[1])
        h_since_midnight_sunset = int(self.sunset_time.split(":")[0]) * 60 + int(self.sunset_time.split(":")[1])
        h_since_midnight_current = self.time_of_day.hour * 60 + self.time_of_day.minute

        minutes_pr_sun_position = (h_since_midnight_sunset - h_since_midnight_sunrise) / self.sun_positions
        self.sun_position = (h_since_midnight_current - h_since_midnight_sunrise) // minutes_pr_sun_position

    def update(self, surface):
        self.draw(surface)

    def draw(self, surface):
        if self.sun_position <= self.sun_positions and self.sun_position >= 1 : #draw sun in pos
            x = self.WIDTH - (self.WIDTH // self.sun_positions * self.sun_position - 1)
            y = self.horizon - (math.sin(self.sun_position / (self.sun_positions - 1) * math.pi) * self.arc_height)
            pygame.draw.circle(surface, (255, 223, 34), (x,y), self.radius)


    
