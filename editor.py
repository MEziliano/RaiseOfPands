import pygame, sys
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
from settings import *

class Editor:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # Navigation
        self.origin = vector()
        self.pan_activate = False
        self.pan_offset = vector()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.pan_input(event)

    def pan_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
            self.pan_activate = True
            self.pan_offset = vector(mouse_pos()) - self.origin
        
        if not mouse_buttons()[1]:
            self.pan_activate = False

        if event.type == pygame.MOUSEWHEEL:
            print(event.y)


        if self.pan_activate:
            self.origin = vector(mouse_pos()) - self.pan_offset
        
    def run(self, dt):
        self.display_surface.fill('white')
        self.event_loop()
        pygame.draw.circle(self.display_surface, 'red', self.origin, 100)
        