import pygame
import random

class Cloud:
    def __init__(self, WIDTH, HEIGHT):
        self.scale = random.randrange(150, 300)

        self.x = random.randrange(-WIDTH - self.scale, WIDTH)

        self.min_y = -self.scale
        self.max_y = HEIGHT * 0.25
        self.distance_min_y_max_y = self.max_y - self.min_y

        self.y = self.min_y + (self.distance_min_y_max_y * random.random() ** 2)

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        whatCloud = random.randrange(0,5)
        clouds = ["CompactPuff.png", "LargeCumulus.png", "LongStratus.png", "Original.png", "TinyPuff.png", "TrailingTail.png"]

        self.image = pygame.transform.smoothscale(pygame.image.load(f'assets/Clouds/{clouds[whatCloud]}') ,(self.scale, self.scale))

        self.movespeed = random.randrange(1, 2)

    def update(self, surface):
        self.x += self.movespeed
        self.draw(surface)
        if self.x > self.WIDTH:
             self.x = random.randrange(-self.WIDTH - self.scale, -self.scale)
             self.y = random.randrange(-self.scale, round(self.HEIGHT * 0.25))

    def draw(self, surface):
            surface.blit(self.image, (self.x, self.y))