# importamos la libreria pygame
import pygame

# inicializamos los modulos de la libreria
pygame.init()

# establecer dimensiones de la ventana
ventana = pygame.display.set_mode((600,360))

#establecer el titulo de la ventana
pygame.display.set_caption("Pygame Guanentá")

# definir colores
azul = (0,0,255)
blanco = (255,255,255)
# creamos una superficie
superficie_1 = pygame.Surface((400,40))
superficie_2 = pygame.Surface((400,40))
superficie_3 = pygame.Surface((400,40))
superficie_4 = pygame.Surface((400,40))
superficie_5 = pygame.Surface((400,40))
superficie_6 = pygame.Surface((600,40))
superficie_7 = pygame.Surface((600,40))
superficie_8 = pygame.Surface((600,40))
superficie_9 = pygame.Surface((600,40))
superficie_10 = pygame.Surface((80,80))
superficie_11 = pygame.Surface((80,80))
superficie_12 = pygame.Surface((80,80))
superficie_13 = pygame.Surface((80,80))
superficie_14 = pygame.Surface((200,40))
superficie_15 = pygame.Surface((40,200))
# rellenamos una superficie de color
superficie_1.fill(azul)
superficie_2.fill(blanco)
superficie_3.fill(azul)
superficie_4.fill(blanco)
superficie_5.fill(azul)
superficie_6.fill(blanco)
superficie_7.fill(azul)
superficie_8.fill(blanco)
superficie_9.fill(azul)
superficie_10.fill(azul)
superficie_11.fill(azul)
superficie_12.fill(azul)
superficie_13.fill(azul)
superficie_14.fill(blanco)
superficie_15.fill(blanco)
# agregar o mover la superficie a la ventana
ventana.blit(superficie_1, (200,0))
ventana.blit(superficie_2, (200,40))
ventana.blit(superficie_3, (200,80))
ventana.blit(superficie_4, (200,120))
ventana.blit(superficie_5, (200,160))
ventana.blit(superficie_6, (0,200))
ventana.blit(superficie_7, (0,240))
ventana.blit(superficie_8, (0,280))
ventana.blit(superficie_9, (0,320))
ventana.blit(superficie_10, (0,0))
ventana.blit(superficie_11, (120,0))
ventana.blit(superficie_12, (0,120))
ventana.blit(superficie_13, (120,120))
ventana.blit(superficie_14, (0,80))
ventana.blit(superficie_15, (80,0))

# actualizar visualizacion de la ventana
pygame.display.flip()

# bucle del juego
while True:
    event = pygame.event.wait()
    if event .type == pygame.QUIT:
        break

pygame.quit()