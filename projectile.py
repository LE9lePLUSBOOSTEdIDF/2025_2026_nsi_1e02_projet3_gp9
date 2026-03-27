import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 0.5
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale_by(self.image, 0.2)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 100

    def remove_projectile(self, player):
        self.player.all_projectiles.remove(self)
        
    def move(self):
        self.rect.x += self.velocity

        if self.rect.x > 1080:
            self.remove_projectile(self)