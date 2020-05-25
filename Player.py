import pygame
from ModelsLoader import *

class Player(object):
    def __init__(self,x,y,width,height,color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = (x, y, width, height)
        self.vel = 5
        self.color = color

    def draw(self, win):
        win.blit(head, (self.x, self.y))
        win.blit(chest,(self.x, self.y))
        #pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        elif keys[pygame.K_RIGHT]:
            self.x += self.vel
        elif keys[pygame.K_UP]:
            self.y -= self.vel
        elif keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)