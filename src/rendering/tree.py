import pygame

class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, wind):
        super().__init__()
        self.scale = scale
        self.wind = wind 
        self.x = x
        self.y = y - self.scale
        
        self.original = pygame.transform.smoothscale(pygame.image.load('assets/originalPixelArtTree.png') ,(self.scale, self.scale))
        self.right = pygame.transform.smoothscale(pygame.image.load('assets/pixelTreeRight.png') ,(self.scale, self.scale))
        self.hardRight = pygame.transform.smoothscale(pygame.image.load('assets/pixelTreeHardRight.png') ,(self.scale, self.scale))
        self.left = pygame.transform.smoothscale(pygame.image.load('assets/pixelTreeLeft.png') ,(self.scale, self.scale))
        self.hardLeft = pygame.transform.smoothscale(pygame.image.load('assets/pixelTreeHardLeft.png') ,(self.scale, self.scale))



        
        self.low_wind_frames = [self.original, self.left, self.original, self.right]
        self.high_wind_frames = [self.original, self.left, self.hardLeft, self.left, self.original, self.right, self.hardRight, self.right]
        
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = scale * 2 - wind * 2

        self.image = self.original 
        
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, surface):
        if self.wind > 10:
            active_frames = self.high_wind_frames
        elif self.wind > 5:
            active_frames = self.low_wind_frames
        else:
            active_frames = None 

        if active_frames is None:
            self.image = self.original
            self.current_frame = 0 
        else:
            current_time = pygame.time.get_ticks()
            
            if current_time - self.last_update > self.animation_cooldown:
                self.current_frame += 1
                
                if self.current_frame >= len(active_frames):
                    self.current_frame = 0
                    
                self.image = active_frames[self.current_frame]
                self.last_update = current_time
        self.draw(self.image, surface)

    def draw(self, image, surface):
        surface.blit(image, (self.x - self.scale / 2, self.y))