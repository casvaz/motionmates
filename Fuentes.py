import pygame
pygame.init()
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)