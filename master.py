import pygame 

pygame.init()


SCREEN_WIDTH  = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.9) 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

x, y    = 200, 200
img     = pygame.image.load()
rect    = img.get_rect()
rect.center = (x,y) 

run = True
while run:



    screen.blit(img, rect)
    for event in pygame.event.get():
        #
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

# https://www.youtube.com/watch?v=DHgj5jhMJKg&list=PLjcN1EyupaQm20hlUE11y9y8EY2aXLpnv