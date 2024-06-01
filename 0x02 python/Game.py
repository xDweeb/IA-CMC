import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Code Quest")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

if __name__ == '__main__':
    run_game()
