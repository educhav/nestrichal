import pygame
import os
from util.constants import PLAYER_HEIGHT, PLAYER_WIDTH

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player_height = PLAYER_HEIGHT
        self.player_width = PLAYER_WIDTH
        self.step = 32
        self.sprite = pygame.image.load(os.path.join("assets", "Elijah.png"))

    def move_left(self):
        self.x -= 32

    def move_right(self):
        self.x += 32

    def move_down(self):
        self.y -= 32

    def move_up(self):
        self.y += 32
