import pygame

class Projectile:
    def __init__(self, x, y, direction):
        self.speed = 10 * direction
        self.damage = 10
        self.image = pygame.image.load("assets/projectile.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(20, 20))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)