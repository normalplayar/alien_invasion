import pygame
import sys
from game_character import Penguin
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Game Character")
    bg_color = (85, 195, 247)
    penguin = Penguin(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        penguin.blitme()
        pygame.display.flip()
run_game()