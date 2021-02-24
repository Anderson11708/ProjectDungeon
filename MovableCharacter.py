import pygame


class MovableCharacter(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.xspeed = 0
        self.yspeed = 0
        self.rect = pygame.Rect(x,y,50,50)

    # draws the enemy
    def draw(self,window):
        pygame.draw.rect(window, (176, 32, 63), self.rect)

    # updates the status of the characters
    def update(self,delta_time,groups):
         self.move(delta_time,groups)


    # the collision physics of the walls
    def move(self, delta_time, groups):
        self.move_y(self.yspeed * delta_time)
        sprite_collision = pygame.sprite.spritecollide(self, groups["wall"], False)
        if sprite_collision:
            if self.yspeed < 0:
                self.set_y(sprite_collision[0].get_bottom())
            if self.yspeed > 0:
                self.set_y(sprite_collision[0].get_top() - 50)
        self.move_x(self.xspeed * delta_time)
        sprite_collision = pygame.sprite.spritecollide(self, groups["wall"], False)
        if sprite_collision:
            if self.xspeed < 0:
                self.set_x(sprite_collision[0].get_right())
            if self.xspeed > 0:
                self.set_x(sprite_collision[0].get_left() - 50)

    # getter and setter methods
    def set_xspeed(self, value):
        self.xspeed = value

    def set_yspeed(self, value):
        self.yspeed = value

    def get_xspeed(self):
        return self.xspeed

    def get_yspeed(self):
        return self.yspeed

    def set_x(self, value):
        self.x = value
        self.rect.x = self.x

    def set_y(self, value):
        self.y = value
        self.rect.y = self.y

    def move_x(self, distance):
        self.x += distance
        self.rect.x = self.x

    def move_y(self, distance):
        self.y += distance
        self.rect.y = self.y




