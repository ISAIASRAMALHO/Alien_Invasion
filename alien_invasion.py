import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():
    pygame.init()
    cfg = Settings()
    screen = pygame.display.set_mode( (cfg.screen_width, cfg.screen_height))
    pygame.display.set_caption('INVASÃO ALIEN')
    nave = Ship(cfg, screen)
    bg_color = (230, 230, 230)
    # lOOP PRINCIPAL
    while True:
        gf.check_events(nave)
        nave.update()
        gf.update_screen( cfg, screen, nave)


# LET'S RUN THE PROGRAMM/GAME
run_game()