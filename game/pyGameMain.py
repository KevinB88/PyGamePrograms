# Example file showing a circle moving on screen
import pygame
import random


def rng(a,b):
    return random.uniform(a, b)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
radius = 40

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    computer_position_1 = pygame.Vector2(50, 50)
    computer_position_2 = pygame.Vector2(150, 150)
    computer_position_3 = pygame.Vector2(250, 250)
    computer_position_4 = pygame.Vector2(500, 500)

    pygame.draw.circle(screen, "black", player_pos, radius)
    pygame.draw.circle(screen, "red", computer_position_1, 10)
    pygame.draw.circle(screen, "red", computer_position_2, 10)
    pygame.draw.circle(screen, "red", computer_position_3, 10)
    pygame.draw.circle(screen, "red", computer_position_4, 10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_q]:
        running = False
    if keys[pygame.K_o]:
        radius += 10
    if keys[pygame.K_p]:
        radius -= 10


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()