#python Setup
import pygame
import sys
import os
import time
import random
from Settings import *
from network import Network
from Player import Player
from ModelsLoader import *
#game window
pygame.init()
resolution = (WIDTH,HEIGHT)
win = pygame.display.set_mode(resolution)
pygame.display.set_caption(TITLE)
mainClock = pygame.time.Clock()

# prepare and open user name and password from auth.txt
file1 = open("auth.txt","r")
auth = {}
authlist = file1.readlines()
authlist = [x.replace('\n', '') for x in authlist]
auth["Username"] = authlist[1]
auth["Password"] = authlist[3]
print(auth)


#ImageLoader


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
def redraw_intro():
    win.blit(introbg,(0,0))
    LogInButton.draw(win,(0,0,0))
    SingInButton.draw(win,(0,0,0))
    pygame.display.update()
def game_intro():
    Intro = True
    while Intro:
        redraw_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Intro = False
            pos = pygame.mouse.get_pos()

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if LogInButton.isOver(pos):
                    #n.send(auth) # sending username and password
                    Intro=False
                elif SingInButton.isOver(pos):
                    #n.send(auth) # sending username and password
                    Intro=False

            if event.type == pygame.MOUSEMOTION:
                if LogInButton.isOver(pos):
                    LogInButton.color = (255,0,0)
                else:
                    LogInButton.color =(0,255,0)
                if SingInButton.isOver(pos):
                    SingInButton.color=(0,0,255)
                else:
                    SingInButton.color=(0,255,0)
def draw_grid(win):
    # tiles of map for easier map making
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(win, LIGHTGREY, (x, 0), (x, HEIGHT))
    for y in range(0, WIDTH, TILESIZE):
        pygame.draw.line(win, LIGHTGREY, (0,y),(WIDTH,y))
def redrawGameWindow():
    win.blit(bg,(0,0))
    draw_grid(win)
    p.draw(win)
    #p2.draw(win)
    pygame.display.update()

#n = Network() communication betwen client and server
#p = n.getP() get position from server
p=Player(0,0,50,50,(255,0,0))
LogInButton = button((0,255,0),50,500,150,75,"Log in")
SingInButton = button((0,255,0),50,600,150,75,"Sign In")
#main loop
def main_loop():
    run=True
    while run:
        mainClock.tick(60)
        #p2 = n.send(p)  #send position to server
       #quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #player movment
        p.move()
        redrawGameWindow()


game_intro()
main_loop()