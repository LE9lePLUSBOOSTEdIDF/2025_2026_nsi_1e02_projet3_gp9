import pygame
from player import Player
from monster import Monster

class Game(): # Création d'une classe générale pour le jeu
    
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        self.pressed = {}

    def check_collisions(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))