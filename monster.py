import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.image = pygame.image.load("assets/monster_skeleton_knight.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1080 + random.randint(100, 300)
        self.rect.y = 200
        self.velocity = random.randint(1, 3)

    def update_health_bar(self, surface):
        bar_position = [self.rect.x + 200, self.rect.y + 100, self.health, 5]
        background_bar_position = [self.rect.x + 200, self.rect.y + 100, self.max_health, 5]

        pygame.draw.rect(surface, (255,255,255), background_bar_position)
        pygame.draw.rect(surface, (0,255,0), bar_position)

    def take_damage(self, damage_amount):
        self.health -= damage_amount
        
        if self.health <= 0:
            self.rect.x = 1080 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1,3)

    def forward(self):
        if not self.game.check_collisions(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.take_damage(self.attack)