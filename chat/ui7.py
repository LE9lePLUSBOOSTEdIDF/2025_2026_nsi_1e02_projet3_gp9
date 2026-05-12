import pygame
from settings import *

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.font.SysFont("Arial", 40)

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect)

        text_surface = self.font.render(self.text, True, WHITE)

        screen.blit(
            text_surface,
            (
                self.rect.x + 20,
                self.rect.y + 10
            )
        )

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)