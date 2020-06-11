import pygame
from pygame.sprite import Sprite

class Balas(Sprite):
    # UM CLASSE QUE ADMINISTRA PROJETÉIS DISPARADOS PELA ESPAÇONAVE.

    def __init__(self, cfg, screen, nave):
        super(Balas, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect( 0,0, cfg.bala_width, cfg.bala_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top
        self.y = float(self.rect.y)
        self.color = cfg.bala_color
        self.speed_factor = cfg.bala_speed_factor

    def upate(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bala(self):
        pygame.draw.rect(self.screen, self.color, self.rect)