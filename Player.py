import pygame
import MovableCharacter


class Player (MovableCharacter.MovableCharacter) :
    def __init__(self):
        super().__init__(400,300)
        self.x = 400
        self.y = 300
        self.xspeed = 0
        self.yspeed = 0
        self.rect = pygame.Rect(0,0,50,50)
        self.color = (39,142,156)

    # collision physics for the health potion
    def update (self, delta_time,groups):
        self.move(delta_time,groups)
        sprite_collision = pygame.sprite.spritecollide(self, groups["health"], True)
        if sprite_collision :
            self.color = (86, 232, 118)
        sprite_collision = pygame.sprite.spritecollide(self, groups["enemies"], False)
        if sprite_collision :
            self.color = (39,142,156)




    # draws the main player
    def draw (self,window) :
        pygame.draw.rect(window,self.color, self.rect)


