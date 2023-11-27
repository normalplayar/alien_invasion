import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((755,600))
    pygame.display.set_caption("Rocket")
    bg_color = (85, 195, 247)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(f"{(event.key)}")
        screen.fill(bg_color)
        pygame.display.flip()

run_game()