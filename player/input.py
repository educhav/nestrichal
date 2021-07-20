import pygame

def handle_input(event, run, player):
    if event.type == pygame.QUIT:
        run = False
        return
    if event.type == pygame.K_w:
        player.move_up()
    if event.type == pygame.K_s:
        player.move_down()
    if event.type == pygame.K_a:
        player.move_left()
    if event.type == pygame.K_d:
        player.move_right()
