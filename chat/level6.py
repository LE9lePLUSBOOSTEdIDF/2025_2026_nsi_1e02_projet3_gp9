import pygame
from settings import *

class Level:
    def __init__(self):
        self.platforms = [
            pygame.Rect(0, 650, 1280, 70),
            pygame.Rect(300, 500, 200, 30),
            pygame.Rect(650, 400, 250, 30),
            pygame.Rect(1000, 300, 150, 30)
        ]

    def handle_collisions(self, player):
        player.on_ground = False

        for platform in self.platforms:
            if player.rect.colliderect(platform):

                if player.vel_y > 0:
                    player.rect.bottom = platform.top
                    player.vel_y = 0
                    player.on_ground = True

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, GRAY, platform)