import pygame
import random

class Star:
    def __init__(self, X, Y, image):
        self.x = X
        self.y = Y
        self.scale = random.randrange(10, 30)
        self.image = pygame.transform.smoothscale(image, (self.scale, self.scale))

    def update(self, screen):
        self.draw(screen)


    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))