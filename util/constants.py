import pygame
import os
from texture.texture import Texture

GAME_WIDTH, GAME_HEIGHT = 800, 608
PLAYER_WIDTH, PLAYER_HEIGHT = 22, 29

TEXTURE_SIZE = 32
TEXTURE_TABLE = {
        "G" : Texture(pygame.image.load(os.path.join("assets", "grass_brush_32x32.png"))),
        "C": Texture(pygame.image.load(os.path.join("assets", "cement_32x32.png"))),
        "B": Texture(pygame.transform.scale(
                    pygame.image.load(os.path.join("assets", "cement_border_16x10.png")), (32, 32))),
        "T": Texture(pygame.transform.rotate(
                    pygame.transform.scale(
                    pygame.image.load(
                    os.path.join("assets", "cement_border_16x10.png")), (32,32)), 180))
        }

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
