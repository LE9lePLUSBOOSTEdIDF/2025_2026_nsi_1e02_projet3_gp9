import pygame
from player import Player
from monster import Monster
from camera import Camera

class Game(): # Création d'une classe générale pour le jeu
    
    def __init__(self):
        self.is_running = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.is_over = False
        self.camera = Camera()
        self.screen = Screen()

    def start_game(self):
        self.is_running = True
        self.is_over = False
        self.spawn_monster()
        self.spawn_monster() # Apparition d'un deuxieme monstre

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.rect.x = -50
        self.player.rect.y = 400
        self.player.all_projectiles = pygame.sprite.Group()
        self.is_running = False
        self.is_over = True

    def update(self):
        self.screen.blit(self.player.image, self.player.rect) # Affichage du sprite 
        self.player.update_health_bar(self.screen)
        #screen.blit(background, (1080, 720))

        self.player.velocity_y += self.player.gravity
        self.player.rect.y += self.player.velocity_y

        if self.player.rect.y >= self.player.ground_level:
            self.player.rect.y = self.player.ground_level
            self.player.velocity_y = 0
            self.player.jump_possibility = True

        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(self.screen)

        self.player.all_projectiles.draw(self.screen)
        self.all_monsters.draw(self.screen)
        self.camera.update(self.player)

        if self.pressed.get(pygame.K_d): #and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()

        elif self.pressed.get(pygame.K_q): #and self.player.rect.x > 0:
            self.player.move_left()       

    def check_collisions(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
        monster.rect.x += self.player.rect.x