import pygame


class House:
    def __init__(self, X, Y, normalList, coldList, Temp, Night):
        self.scale = 400
        self.x = X
        self.y = Y - self.scale
        self.tempThreshold = 10
        self.temp = Temp
        self.night = Night

        self.normal = normalList
        self.cold = coldList
        self.smoke_frame = 1


    def update(self, screen):
        if self.temp < self.tempThreshold:
            image = pygame.transform.smoothscale(self.cold[self.smoke_frame // 10 - 1] ,(self.scale, self.scale))
            self.smoke_frame += 1
            if self.smoke_frame > 90:
                self.smoke_frame = 1
        elif self.night:
            image = pygame.transform.smoothscale(self.normal["HouseNight"] ,(self.scale, self.scale))
        else:
            image = pygame.transform.smoothscale(self.normal["HouseOriginal"] ,(self.scale, self.scale))
            
        self.draw(screen, image)

    def draw(self, screen, image):
        screen.blit(image, (self.x, self.y))
