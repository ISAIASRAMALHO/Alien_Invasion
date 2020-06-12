import sys
import pygame
from bullet import Balas
from pygame.sprite import Sprite

def check_events(cfg, screen, nave, balas):
    # RESPONDE A EVENTOS DE PRESSIONAMENTO DE TECLAS E MOUSE.
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            nova_bala = Balas( cfg, screen, nave)
            balas.add( nova_bala )
        nave.moving_right = ( event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT )
        nave.moving_left  = ( event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT )

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         nave.moving_right = True
        #     elif event.key == pygame.K_LEFT:
        #         nave.moving_left = True
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_RIGHT:
        #         nave.moving_right = False
        #     elif event.key == pygame.K_LEFT:
        #         nave.moving_left = False


def update_screen(cfg, screen, nave, balas):
    # ATUALIZA AS IMAGENS DA TELA E ALTERA PARA A NOVA TELA.
    screen.fill(cfg.bg_color)
    for b in balas.sprites():
        b.draw_bala()
    nave.blitme()
    pygame.display.flip()
