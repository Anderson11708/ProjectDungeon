import pygame


class SpriteSheet :
    def __init__(self,Tiles, size):
        self.sheet = pygame.image.load(Tiles)
        self.size = size
    # gets the sprite that we are using
    def get_sprite (self,x,y):
        rect = pygame.Rect(x*16,y*16,self.size,self.size)
        image = pygame.Surface((self.size,self.size))
        image.blit(self.sheet,(0,0),rect)
        return image
