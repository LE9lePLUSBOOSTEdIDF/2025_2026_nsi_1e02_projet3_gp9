import pygame

class Player(pygame.sprite.Sprite): # Création de la classe joueur

    def __init__(self):
        super().__init__() # Association du joueur avec une image
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 10
        self.image = pygame.image.load("assets/knight_sprite.png") # Chargement de l'image du joueur
        self.rect = self.image.get_rect() # Récupération de la position du joueur
        self.rect.x = -50
        self.rect.y = 100

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity        