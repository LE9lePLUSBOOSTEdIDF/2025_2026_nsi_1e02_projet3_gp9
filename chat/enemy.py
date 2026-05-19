import pygame

class Enemy:
    def __init__(self, x, y):
        self.speed = 2
        self.health = 50
        self.damage = 10
        self.image = pygame.transform.scale_by(pygame.image.load("assets/monster_skeleton_knight.png").convert_alpha(), 0.20)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.x -= self.speed

        if self.rect.left <= 0 or self.rect.right >= 1280:
            self.speed *= -1
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

        pygame.draw.rect(screen, (255, 0, 0),
                         (self.rect.x, self.rect.y - 10, 50, 5))

        pygame.draw.rect(screen, (0, 255, 0),
                         (self.rect.x, self.rect.y - 10, self.health, 5))