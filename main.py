import pygame
from game.constants import GAME_WIDTH, GAME_HEIGHT
from game.game import Game

pygame.display.set_caption("Nestrichal")

FPS = 120
WINDOW = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

clock = pygame.time.Clock()
game = Game(WINDOW)

def main():
    while True:
        dt = clock.tick(FPS)
        game.update(dt)
main()
