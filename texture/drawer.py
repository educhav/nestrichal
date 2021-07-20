from .map import WORLD_MAP
from util.constants import TEXTURE_TABLE, TEXTURE_SIZE, GAME_WIDTH, GAME_HEIGHT

def draw_map(WINDOW):
    x = 0
    y = 0
    for row in WORLD_MAP:
        for key in row:
            texture = TEXTURE_TABLE[key]
            WINDOW.blit(texture.image, (x, y))
            x += TEXTURE_SIZE
            if x >= GAME_WIDTH:
                x = 0
                break
        y += TEXTURE_SIZE
        if y >= GAME_HEIGHT:
            y = 0
            break

def draw_window(WINDOW):
    draw_map(WINDOW)
