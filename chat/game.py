import pygame
import sys

from settings import *
from player import Player
from enemy import Enemy
from level import Level
from ui import Button

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        self.state = "menu"

        self.start_button = Button(500, 300, 300, 80, "JOUER")
        self.retry_button = Button(500, 300, 300, 80, "REESSAYER")

        self.font = pygame.font.SysFont("Arial", 32)

        self.reset_game()

        self.background = pygame.image.load("assets/background_castle.png").convert()
        self.background = pygame.transform.scale(
            self.background,
            (WIDTH, HEIGHT)
        )

    def reset_game(self):
        self.player = Player(100, 500)

        self.enemies = [
            Enemy(700, 550),
            Enemy(1000, 550),
            Enemy(850, 300)
        ]

        self.level = Level()

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            if self.state == "menu":
                self.menu_events()
                self.menu_draw()

            elif self.state == "game":
                self.game_events()
                self.update()
                self.draw()

            elif self.state == "dead":
                self.dead_events()
                self.dead_draw()

            pygame.display.flip()

        pygame.quit()
        sys.exit()
        
    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.is_clicked(event.pos):
                    self.state = "game"

    def dead_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.retry_button.is_clicked(event.pos):
                    self.reset_game()
                    self.state = "game"

    def game_events(self):
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

                if event.key == pygame.K_f:
                    self.player.shoot()

                if event.key == pygame.K_e:
                    attack_rect = self.player.melee_attack()

                    if attack_rect:
                        for enemy in self.enemies:
                            if attack_rect.colliderect(enemy.rect):
                                enemy.health -= 20

        self.player.handle_input(keys)
    
    def update(self):
        self.player.update()

        self.level.handle_collisions(self.player)

        for enemy in self.enemies:
            enemy.update()

            if enemy.rect.colliderect(self.player.rect):
                self.player.health -= 0.1

        for projectile in self.player.projectiles[:]:
            for enemy in self.enemies:
                if projectile.rect.colliderect(enemy.rect):
                    enemy.health -= projectile.damage
                    enemy.check_health()

                    if projectile in self.player.projectiles:
                        self.player.projectiles.remove(projectile)

                    self.enemies = [e for e in self.enemies if e.health > 0]

        if self.player.health <= 0:
            self.state = "dead"

    def draw_hud(self):
        hp_text = self.font.render(
            f"Vie Joueur : {int(self.player.health)}",
            True,
            WHITE
        )

        self.screen.blit(hp_text, (20, 20))

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.level.draw(self.screen)

        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        self.draw_hud() 
    
    def menu_draw(self):
        self.screen.fill((20, 20, 20))

        title = self.font.render("CASTLE CAVE", True, WHITE)

        self.screen.blit(title, (520, 200))

        self.start_button.draw(self.screen)

    def dead_draw(self):
        self.screen.fill((0, 0, 0))

        dead_text = self.font.render("VOUS ETES MORT", True, RED)

        self.screen.blit(dead_text, (500, 200))

        self.retry_button.draw(self.screen)
