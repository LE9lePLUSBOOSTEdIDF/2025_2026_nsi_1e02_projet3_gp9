import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/monster_skeleton_knight.png")
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 200
        self.velocity = 1

    def forward(self):
        if not self.game.check_collisions(self, self.game.all_players):
            self.rect.x -= self.velocity