import pygame

class Projectile:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, 12, 6)
        self.speed = 10 * direction
        self.damage = 10

    def update(self):
        self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)