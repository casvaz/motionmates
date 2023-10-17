import pygame
from pygame.locals import *
import sys

# PAGINA PRINCIPAL

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 350

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

def crear_boton(superficie, texto, x, y, radio, color_fondo, color_texto, accion):
    pygame.draw.rect(superficie, color_fondo, pygame.Rect(x - radio, y - radio, radio * 2, radio * 2), border_radius=radio)
    fuente = pygame.font.Font('BRLNSB.ttf', 20)
    texto_renderizado = fuente.render(texto, True, color_texto)
    texto_rect = texto_renderizado.get_rect(center=(x, y))
    superficie.blit(texto_renderizado, texto_rect)
    
    if distancia(x, y, pygame.mouse.get_pos()) < radio and pygame.mouse.get_pressed()[0] and accion:
        accion()

def distancia(x1, y1, pos):
    return ((x1 - pos[0]) ** 2 + (y1 - pos[1]) ** 2) ** 0.5

def iniciar_sesion():
    print("Iniciar sesión")
    
def main():
    # Inicia el programa
    pygame.init()
    # Creación de ventana y título
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("MotionMates")
    
    # Titulos
    fuente = pygame.font.Font('CASTELAR.ttf', 28)
    texto = fuente.render('MOTIONMATES', True, (255, 255, 255))
    
    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Dibujar un rectángulo blanco a la derecha
        '''rectangulo_blanco = pygame.Rect(500, 0, 300, SCREEN_HEIGHT)
        pygame.draw.rect(screen, (255, 255, 255), rectangulo_blanco)'''
        
        # Fondo e imagen
        fondo = pygame.image.load("azul.jpg").convert()
        tux = pygame.image.load("fisio.png").convert_alpha()    
        
        screen.blit(fondo, (0, 0))
        screen.blit(tux, (8, 15))
        screen.blit(texto, (28, 275))
        crear_boton(screen, "Iniciar Sesión", 400, 250, 50, AZUL, BLANCO, iniciar_sesion)
        pygame.display.flip()

if __name__ == "__main__":
    main()
