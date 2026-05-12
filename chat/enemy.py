import pygame

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = 2
        self.health = 50
        self.damage = 10

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 50, 50), self.rect)

        pygame.draw.rect(screen, (255, 0, 0),
                         (self.rect.x, self.rect.y - 10, 50, 5))

        pygame.draw.rect(screen, (0, 255, 0),
                         (self.rect.x, self.rect.y - 10, self.health, 5))