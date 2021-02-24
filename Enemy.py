import pygame
import MovableCharacter
class Enemy (MovableCharacter.MovableCharacter):
    def __init__(self,x,y):
        super().__init__(x,y)
        #normal speed is 100
        self.xspeed = 50


    def update (self,delta_time,groups):
        self.move(delta_time,groups )