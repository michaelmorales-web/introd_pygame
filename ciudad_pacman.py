# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

import pygame 
import sys
import math

PI = math.pi

negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255,165,0)
verde = (0,255,0)
rosado = (255,192,203)
amarillo = (255,255,0)
blanco = (255,255,255)
cian = (0,255,255)

ventana = pygame.display.set_mode((1000,400))

pygame.display.set_caption("Bambiland")

pygame.init()

while True:

    for event in pygame.event.get():
        # Al hacer click sobre el boton de cerrar la ventana el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(negro)

    # Rueda de la fortuna
    pygame.draw.circle(ventana, blanco, (100,200), 100, 5)
    pygame.draw.line(ventana, blanco, (0,400),  (100,200), 5)
    pygame.draw.line(ventana, blanco, (200,400), (100,200), 5)

    # Montaña rusa
    puntos_1 = [(250,400), (400,380), (500,200), (600,380), (750,400)]
    pygame.draw.lines(ventana, azul, False, puntos_1, 5)
    

    # Letrero de el lugar
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("Bambiland",1,blanco)
    ventana.blit(texto, (200,30))

    # actualizar visualización de la ventana
    pygame.display.flip()