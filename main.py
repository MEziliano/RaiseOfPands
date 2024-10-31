# creating a window with pytgame 
# An ultimate guide to pygame
import pygame
from sys import exit

pygame.init() # Responsable to start stuffs
# display surface creating our window
screen = pygame.display.set_mode((800, 400)) # weight x height 
pygame.display.set_caption("The Raise of Pands")
# create a clock
clock = pygame.time.Clock() # import to be Capital
# Create font style 
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # (Font_type , size)

# Create and changing the Surface 
### First attempt
#test_surface = pygame.Surface((100,200)) # import to be Capital
#test_surface.fill('Red') # Reference https://www.pygame.org/docs/ref/color_list.html
test_surface = pygame.image.load('graphics/Sky.png').convert() # Specify the path
#When you upload a surface you did separated by the window
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("The Raise of Pands", False, 'Pink')


# import snail
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha() # convert can be use to png files 
snail_x_pos = 600

# import surface player
player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom= (80,300))


while True: # it will run forever
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #draw all our elements#update everything
    """
    So far we can create a windown, but a message error has appeear in the terminal
    pygame.error: video system not initialized
    Why? pygame.quit with pygame.update made it 
    So, the answer for this issue is import sys and use exit
    """
    
    screen.blit(test_surface, (0,0))# Block image transform (surface,position), but in black
    screen.blit(ground_surface, (0,300))
    # When it get some color will be at the position marked 
    screen.blit(text_surface, (300,50))
    snail_x_pos -= 2
    if snail_x_pos < - 100: snail_x_pos = 800 
    screen.blit(snail_surface, (snail_x_pos, 250))
    player_rect.left +=1
    screen.blit(player_surface,player_rect)

    
    pygame.display.update()
    clock.tick(60) # Responsable for the game don't run to fast

    # Surface >> Display Surface >> (Regular) surfacef
    
