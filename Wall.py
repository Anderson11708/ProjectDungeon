import pygame
import SpriteSheet
sheet = SpriteSheet.SpriteSheet("img/Dungeon_Tileset.png",16)

class Wall (pygame.sprite.Sprite):
    # x = the x position of the sprite on screen
    # y = the y position of the sprite on screen
    # sprite_x = x position of the sprite in the sprite sheet
    # sprite_y = y position of the sprite in the sprite sheet
    def __init__(self,x,y,sprite_x,sprite_y,):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,50,50)
        self.sprite = 0
        self.set_sprite(sprite_x,sprite_y)
    # draws a single wall
    def draw (self,window):
        window.blit(self.sprite, (self.x,self.y))
    #gets the boundary of the wall sprite
    def get_bottom(self):
        return self.rect.bottom
    def get_top(self):
        return self.rect.top
    def get_right(self):
        return self.rect.right
    def get_left(self):
        return self.rect.left
    # chooses what sprite we are using
    # x and y is the position on the tile set defined in the constructor
    def set_sprite(self,x,y):
        self.sprite = sheet.get_sprite(x,y)
        self.sprite = pygame.transform.scale(self.sprite, (50,50))




# draws every single wall based on the parameters provided
# x and y determines the starting position of the sprite
# w and h defines how many sprites are drawn in the window
# sprite_x and sprite_y determines what sprite we are using
# always generates walls in a rectangular fashion
def generate_walls(x,y,w,h,sprite_x,sprite_y):
    wall_group = pygame.sprite.Group()
    for j in range (h):
        for i in range (w):
            wall_group.add(Wall(x+(50*i),(y+(50*j)),sprite_x,sprite_y))
    return wall_group
