
import pygame
from pygame.locals import *
import random
from sys import exit

pygame.init()
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Desenhando Retângulos")

# Função para desenhar retângulos em posições aleatórias
def draw_random_rectangles(surface, num_rects=10):
    for _ in range(num_rects):
        rect_width = random.randint(20, 70)
        rect_height = random.randint(20, 70)
        x = random.randint(0, SCREEN_SIZE[0] - rect_width)
        y = random.randint(0, SCREEN_SIZE[1] - rect_height)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.rect(surface, color, (x, y, rect_width, rect_height))

# Variável para controlar se os retângulos devem aparecer
rectangles_visible = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_x:  # Se a tecla 'X' for pressionada
                rectangles_visible = False

    screen.fill((0, 0, 0))  # Limpa a tela preenchendo com preto
    
    if rectangles_visible:
        draw_random_rectangles(screen)  # Desenha os retângulos na tela

    pygame.display.update()
