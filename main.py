import pygame
from nestrichal.constants import GAME_WIDTH, GAME_HEIGHT
from nestrichal.player import PLAYER

FPS = 60
WINDOW = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
BG = pygame.image.load("assets/background_alley.png")

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        WINDOW.blit(BG, (0, 0))
        pygame.display.set_caption("Nestrichal")
        pygame.display.update()
    pygame.quit()

main()
