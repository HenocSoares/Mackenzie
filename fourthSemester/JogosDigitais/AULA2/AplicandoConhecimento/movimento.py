import pygame
from pygame.locals import *
import math
from sys import exit

pygame.init()
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

# Carrega a imagem do tanque
tanque_original = pygame.image.load('tanque.jpg').convert_alpha()
tanque = tanque_original.copy()
rect_tanque = tanque.get_rect()

# Inicializa a posição e a rotação do tanque
x, y = SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2
angulo = 0

# Velocidade de rotação e movimento do tanque
vel_rotacao = 2
vel_movimento = 5

# Função para rotacionar o tanque
def rotacionar_tanque(angulo):
    return pygame.transform.rotate(tanque_original, angulo)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    teclas = pygame.key.get_pressed()

    # Verifica as teclas direcionais pressionadas e ajusta a rotação do tanque
    if teclas[K_LEFT]:
        angulo += vel_rotacao
    if teclas[K_RIGHT]:
        angulo -= vel_rotacao

    # Calcula a direção do movimento com base no ângulo do tanque
    mov_x = vel_movimento * math.cos(math.radians(angulo))
    mov_y = vel_movimento * math.sin(math.radians(angulo))

    # Ajusta a posição do tanque com base nas teclas direcionais invertidas
    if teclas[K_UP]:
        x -= mov_x
        y += mov_y
    if teclas[K_DOWN]:
        x += mov_x
        y -= mov_y

    # Rotaciona o tanque de acordo com o ângulo atual
    tanque = rotacionar_tanque(angulo)
    rect_tanque = tanque.get_rect(center=(x, y))

    screen.fill((255,255,255))
    screen.blit(tanque, rect_tanque)

    pygame.display.update()
