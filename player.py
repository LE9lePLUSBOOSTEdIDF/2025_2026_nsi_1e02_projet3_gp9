import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite): # Création de la classe joueur

    def __init__(self, game):
        self.game = game
        super().__init__() # Association du joueur avec une image
        self.sprite = pygame.image.load("assets/knight_sprite.png") # Chargement de l'image du joueur
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.transform.scale_by(self.sprite, 0.35)
        self.rect = self.image.get_rect() # Récupération de la position du joueur
        self.rect.x = -50
        self.rect.y = 400

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        if not self.game.check_collisions(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity        