import pygame, sys
from pygame.math import Vector2 as vector
from settings import *

class Editor:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # Navigation
        self.origin = vector()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pan_input(event)

    def pan_input(self, event):
        
        

    def run(self, dt):
        self.display_surface.fill('white')
        self.event_loop()
        