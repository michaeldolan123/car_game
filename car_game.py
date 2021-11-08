import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 120
clock = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

width = 400
height = 600

DISPLAYSURF = pygame.display.set_mode((width, height))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Car Game")

while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
