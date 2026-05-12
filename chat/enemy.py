import pygame

class Enemy:
    def __init__(self, x, y):
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.health = 50
        self.damage = 10
        self.image = pygame.image.load("assets/monster_skeleton_knight.png").convert_alpha()
        self.image = pygame.transform.scale(
        self.image,
        (70, 70)
        )

    def update(self):
        self.rect.x -= self.speed
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

        pygame.draw.rect(screen, (255, 0, 0),
                         (self.rect.x, self.rect.y - 10, 50, 5))

        pygame.draw.rect(screen, (0, 255, 0),
                         (self.rect.x, self.rect.y - 10, self.health, 5))