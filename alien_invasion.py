import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    cfg = Settings()
    screen = pygame.display.set_mode( (cfg.screen_width, cfg.screen_height))
    pygame.display.set_caption('INVASÃO ALIEN')
    nave = Ship(cfg, screen)
    balas = Group()
    bg_color = (230, 230, 230)
    # lOOP PRINCIPAL
    while True:
        gf.check_events(cfg, screen, nave, balas)
        nave.update()
        balas.update()
        gf.update_screen( cfg, screen, nave, balas)


# LET'S RUN THE PROGRAMM/GAME
run_game()