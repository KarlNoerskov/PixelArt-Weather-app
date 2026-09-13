import random
import pygame
import math

class Wind:
    def __init__(self, Wind, WIDTH, HEIGHT, Image):
        self.scale = random.randrange(10, 60)

        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

        self.x = random.randrange(-self.scale - WIDTH, -self.scale)
        self.y = random.randrange(HEIGHT- HEIGHT // 3, HEIGHT - self.scale)

        self.base_x = self.x
        self.base_y = self.y


        self.angle = random.uniform(0, 6.28)
        self.circle_radius = 0.5
        self.circle_speed = 0.05

        self.image = pygame.transform.smoothscale(Image ,(self.scale, self.scale))

        self.wind = Wind

    def update(self, surface):
        self.x += self.wind

        self.angle += self.circle_speed
        self.x += math.cos(self.angle) * self.circle_radius
        self.y += math.sin(self.angle) * self.circle_radius

        self.draw(surface)
        if self.x > self.WIDTH:
            self.x = random.randrange(-self.scale - self.WIDTH, -self.scale)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))