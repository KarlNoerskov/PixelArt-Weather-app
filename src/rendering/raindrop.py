import pygame
import random
import math

class Raindrop:
    def __init__(self, screen_width, wind_speed, Image):
        self.x = random.randint(-1200, screen_width+200)
        self.y = random.randint(-50, 0)
        
        self.y_vel = random.uniform(5, 10) 
        
        self.x_vel = wind_speed * 0.5 

        self.image = Image

    def calculate_angle(self):
        return math.degrees(math.atan2(self.x_vel, self.y_vel))


    def fall(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self, surface):
        image = pygame.transform.rotate(self.image, self.calculate_angle())
        surface.blit(image, (self.x, self.y))
