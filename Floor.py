import pygame
import SpriteSheet
sheet = SpriteSheet.SpriteSheet("img/Dungeon_Tileset.png",16)
# works almost the same when it comes to generating the sprites

class Floor (pygame.sprite.Sprite) :

    def __init__(self, x, y,sprite_x,sprite_y):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,50,50)
        self.sprite = 0
        self.set_sprite(sprite_x,sprite_y)


    def draw(self, window):
        window.blit(self.sprite,(self.x, self.y))


    def set_sprite (self,x,y):
        self.sprite = sheet.get_sprite(x, y)
        self.sprite = pygame.transform.scale(self.sprite, (50,50))


def generate_floor(x, y, w, h, sprite_x, sprite_y):
    floor_group = pygame.sprite.Group()
    for j in range(h):
        for i in range(w):
            floor_group.add(Floor(x+(50*i), (y + (50 * j)), sprite_x, sprite_y))
    return floor_group
