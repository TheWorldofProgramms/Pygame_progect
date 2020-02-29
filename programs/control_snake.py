import pygame
from pygame.locals import *

class Control:
    def __init__(self):
        self.done = True
        self.flag_direction = "Right"
        self.fl_pause = False
        self.ng = False
        self.end = False

    def control(self):
        #Упарвление в зависимости от флага
        for e in pygame.event.get():
            if e.type == QUIT:
                self.done = False
            elif e.type == KEYDOWN:
                if e.key == K_RIGHT and self.flag_direction != "Left":
                    self.flag_direction = "Right"
                elif e.key == K_LEFT and self.flag_direction != "Right":
                    self.flag_direction = "Left"
                elif e.key == K_UP and self.flag_direction != "Down":
                    self.flag_direction = "Up"
                elif e.key == K_DOWN and self.flag_direction != "Up":
                    self.flag_direction = "Down"
                elif e.key == K_ESCAPE:
                    self.done = False
                elif e.key == K_p:
                    if self.fl_pause:
                        self.fl_pause = False
                    else:
                        self.fl_pause = True
                elif e.key == K_n:
                    self.end = True
                elif e.key == K_y:
                    self.ng = True
