import pygame, os
from util.constants import GAME_WIDTH, GAME_HEIGHT
from player.player import Player
from player.input import handle_input
from texture.drawer import draw_window

FPS = 60
WINDOW = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
# BACKGROUND = pygame.image.load(os.path.join("assets", ""))

def main():
    run = True
    clock = pygame.time.Clock()
    player = Player(300, 300)

    while run:
        clock.tick(FPS) 
        for event in pygame.event.get():
            handle_input(event, run, player)

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        draw_window(WINDOW)
        pygame.display.set_caption("Nestrichal")
        pygame.display.update()
    pygame.quit()

main()
