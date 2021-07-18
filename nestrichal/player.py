import pygame
from .constants import *

FRONT = pygame.image.load("Elijah.png")
RIGHT = pygame.image.load("Elijah_right.png")

class Player:
    def __init__(self):
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT // 2
        self.player_height = PLAYER_HEIGHT
        self.player_width = PLAYER_WIDTH
