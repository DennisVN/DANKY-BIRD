import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((576, 1024)) #pixels van het scherm
clock = pygame.time.Clock() #FPS instellen

bg_surface = pygame.image.load('assets/background-day.png')

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #rode kruiske toevoegen om canvas te sluiten. 
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface,(0,0))

    pygame.display.update()
    clock.tick(120) #120 FPS