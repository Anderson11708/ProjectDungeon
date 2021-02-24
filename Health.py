import pygame
import SpriteSheet

class Health (pygame.sprite.Sprite) :
    image = 0
    def __init__(self, x,y):
        super().__init__()
        self.x =  x
        self.y =  y
        self.rect = pygame.Rect(x,y, 48,48)
        if Health.image == 0 :
            self.set_image()
    # draws the sprite
    def draw (self, window):
        window.blit(Health.image, (self.x, self.y))



    # sets the sprite we are going to use
    def set_image (self):
        sheet = SpriteSheet.SpriteSheet("img/Dungeon_Tileset.png",16)
        Health.image = sheet.get_sprite(9,8)
        Health.image = pygame.transform.scale(Health.image,(48,48))