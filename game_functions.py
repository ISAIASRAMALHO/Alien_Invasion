import sys
import pygame

def check_events(nave):
    # RESPONDE A EVENTOS DE PRESSIONAMENTO DE TECLAS E MOUSE.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                nave.moving_right = True
            elif event.key == pygame.K_LEFT:
                nave.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                nave.moving_right = False
            elif event.key == pygame.K_LEFT:
                nave.moving_left = False


def update_screen(cfg, screen, nave):
    # ATUALIZA AS IMAGENS DA TELA E ALTERA PARA A NOVA TELA.
    screen.fill(cfg.bg_color)
    nave.blitme()
    pygame.display.flip()
