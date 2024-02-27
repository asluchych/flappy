import pygame
from pygame.sprite import Group
from settings import *

class BG(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        bg_image = pygame.image.load('./graphics/environment/background.png').convert()

        full_height = bg_image.get_height() * scale_factor
        full_width = bg_image.get_width() * scale_factor

        self.image = pygame.transform.scale(bg_image, (full_width, full_height))
        self.rect = self.image.get_rect(topleft = (0,0))
