import pygame

pygame.init()

# Global constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

running = True
while running:

    # Exit the Game, if user clicks the windows close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(WHITE)

    circle_center = (250, 250)
    circle_radius = 75
    pygame.draw.circle(SCREEN, BLUE, circle_center, circle_radius)

    pygame.display.flip()

pygame.quit()
