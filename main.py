import pygame
from sys import exit

window_width = 1280
window_height = 720

pygame.init() 
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("CHARACTER DISPLAY")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    window.fill((14, 2, 26))
    pygame.display.update()
    clock.tick(60)
