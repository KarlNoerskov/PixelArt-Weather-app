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


    def fall(self, surface, raindrop_effect_particles):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.y >= 800:
            self.particle_effect(raindrop_effect_particles)

    def draw(self, surface):
        image = pygame.transform.rotate(self.image, self.calculate_angle())
        surface.blit(image, (self.x, self.y))

    def particle_effect(self, particles_list):
        for _ in range(5):
            # Tilføjer nye partikler til hovedlisten
            particles_list.append(Particle(self.x, self.y))


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_vel = random.uniform(-2, 2)   # Spreder sig til siderne
        self.y_vel = random.uniform(-5, -2)  # Hopper lidt opad (negativ y)
        self.timer = 15                      # Lever i 15 frames

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.timer -= 1

    def draw(self, surface):
        pygame.draw.circle(surface, (102, 212, 249), (int(self.x), int(self.y)), 2)