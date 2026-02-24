import pygame
import random
from sys import exit

# config
window_width = 1280
window_height = 720
border_color = (108, 99, 255)
bg_color = (18, 8, 32)

border = 20
text_x = 40
text_gap = 16

# setup
pygame.init() 
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("CHARACTER DISPLAY")
clock = pygame.time.Clock()

font_small = pygame.font.Font("assets/fonts/SpaceMono-Regular.ttf", 14)

# scanlines
def create_scanlines(size):
    surf = pygame.Surface(size).convert_alpha()
    surf.fill((0,0,0,0))

    for j in range(0, size[1], 4):
        surf.fill((0,0,0,40), (0, j, size[0], 1))

    return surf

SCANLINES = create_scanlines((window_width, window_height))

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # bg & overlay
    window.fill(bg_color)
    window.blit(SCANLINES, (0, 0))

    # border text
    topline = font_small.render("HRKRN.BUILD / PROJECTS/", True, border_color)
    text_width = topline.get_width()

    # frame
    pygame.draw.line(window, border_color, (border, border), (text_x - text_gap, border), 1)
    pygame.draw.line(window, border_color, (text_x + text_width + text_gap, border), (window_width - border, border), 1)
    pygame.draw.line(window, border_color, (border, border), (border, window_height - border), 1)
    pygame.draw.line(window, border_color, (window_width - border, border), (window_width - border, window_height - border), 1)
    pygame.draw.line(window, border_color, (border, window_height - border), (window_width - border, window_height - border), 1)

    window.blit(topline, (text_x, border - 9))

    # glitch lines
    if random.randint(0, 120) == 0:
        for _ in range(random.randint(1, 5)):
            y = random.randint(0, window_height)
            offset = random.randint(2, 10)
            pygame.draw.rect(window, (60, 55, 80), (offset, y, window_width, 1))

    pygame.display.update()
    clock.tick(60)