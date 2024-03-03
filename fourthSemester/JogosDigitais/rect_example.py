import pygame

# initialize
pygame.init( )

# screen details
screen_width = 1800
screen_height = 1400
screen = pygame.display.set_mode((screen_width, screen_height))

# defining color to red
colorRect = (255, 0, 0)

# draw.rect = screen, color, position (40, 40), size (90, 30), and border thickness = 3
pygame.draw.rect(screen, colorRect, (40, 40, 90, 30), 3)

# update the display
pygame.display.flip( )

# event loop to keep the window open
running = True
while running:
    for event in pygame.event.get( ):
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit( )
