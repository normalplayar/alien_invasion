import sys
import pygame
from game_character import Rocket
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((755,600))
    pygame.display.set_caption("Rocket")
    bg_color = (85, 195, 247)
    rocket = Rocket(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                # Move the ship to the right.
                    rocket.moving_right = True
                elif event.key == pygame.K_a:
                # Move the ship to the left.
                    rocket.moving_left = True
                elif event.key == pygame.K_w:
                # Move the ship to the up.
                    rocket.moving_up = True
                elif event.key == pygame.K_s:
                # Move the ship to the down.
                    rocket.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    rocket.moving_right = False
                elif event.key == pygame.K_a:
                    rocket.moving_left = False
                elif event.key == pygame.K_w:
                    rocket.moving_up = False
                elif event.key == pygame.K_s:
                    rocket.moving_down = False
        rocket.update()
        screen.fill(bg_color)
        rocket.blitme()
        pygame.display.flip()

run_game()