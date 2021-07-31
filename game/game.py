from .__init__ import pygame, os, scale, load
from .constants import GAME_WIDTH, GAME_HEIGHT, BLACK, WHITE, NARROW
import sys

pygame.font.init()

class Player:
    def __init__(self, x, y, max_hp):
        self.x = x
        self.y = y
        self.velocity = 1
        self.max_hp = max_hp
        self.player_height = 64
        self.player_width = 64
        self.sprite = scale(load(os.path.join("assets", "sprites", "Elijah.png")),
                            (self.player_width, self.player_height))
        self.current_state = 0
        self.states = 0
        self.animations = 0

    def draw(self, window):
        window.blit(self.sprite, (self.x, self.y))

class Scene:
    def __init__(self, window, scene_number):
        self.window = window
        self.scene_number = scene_number
        self.background = load(os.path.join("assets", "background", "town_demo.png"))
        self.master = Player(300, 300, 100)
        self.slaves = []

    def draw_bg(self):
        self.window.blit(self.background, (0, 0))

    def render_text(self, text, image, image_position, size, color, 
                    x_spacing, y_spacing, 
                    left_offset, right_offset, 
                    top_offset, bottom_offset, tick):
        font = pygame.font.Font(os.path.join("assets", "fonts", "pixel_font.ttf"), size)
        x = left_offset
        y = top_offset
        words = text.split(" ")
        add_space = lambda word : word + " " 
        words = [add_space(word) for word in words]
        for word in words:
            if y + y_spacing >= GAME_HEIGHT - bottom_offset:
                self.window.blit(image, image_position)
                y = top_offset
                x = left_offset
            elif x + (len(word) * x_spacing) >= GAME_WIDTH - right_offset:
                x = left_offset
                y += y_spacing
            for char in word:
                text_image = font.render(str(char), 1, color)
                self.window.blit(text_image, (x, y))
                x += x_spacing
                if str(char) in NARROW:
                    x -= x_spacing / 2
                pygame.time.delay(tick)
                pygame.display.update()

    def fade_out(self):
        fading = None
        alpha = 0
        veil = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        veil.fill((0, 0, 0))

    def fade_in(self, bg):
        pass

    def run(self):
        if self.scene_number == 0:
            f = open(os.path.join("scripts", "scene0", "scene0.txt"))
            intro_script = str(f.read())
            black_bg = load(os.path.join("assets", "background", "black_bg.png"))
            self.render_text(intro_script, 
                            image=black_bg, image_position=(0,0), 
                            size=24, color=WHITE, 
                            x_spacing=15, y_spacing=25, 
                            left_offset=15, right_offset=15, 
                            top_offset=15, bottom_offset=75, tick=2)
            self.fade_out()

class Game:
    def __init__(self, window):
        self.window = window
        self.scenes = [Scene(self.window, 0)]
        self.current_scene = self.scenes[0]

    def handle(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys_pressed = pygame.key.get_pressed()
        player = self.current_scene.master
        if keys_pressed[pygame.K_w]:
            player.y -= player.velocity * (dt / 5)
        if keys_pressed[pygame.K_s]:
            player.y += player.velocity * (dt / 5)
        if keys_pressed[pygame.K_a]:
            player.x -= player.velocity * (dt / 5)
        if keys_pressed[pygame.K_d]:
            player.x += player.velocity * (dt / 5)
            
    def update(self, dt):
        self.handle(dt)
        self.scenes[0].draw_bg()
        self.scenes[0].master.draw(self.window)
        pygame.display.update()
