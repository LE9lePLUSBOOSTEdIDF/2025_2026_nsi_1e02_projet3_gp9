import pygame
from settings import *
from projectile import Projectile

class Player:
    def __init__(self, x, y):
        self.projectiles = []

        self.attack_damage = 20
        self.attack_cooldown = 0
        self.shoot_cooldown = 0

        self.health = 100

        self.vel_y = 0
        self.on_ground = False

        self.direction = 1

        self.initial_image = pygame.transform.scale_by(pygame.image.load("assets/knight_sprite.png").convert_alpha(), 0.25)
        self.image = pygame.image.load("assets/knight_sprite.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.25)

        self.rect = self.image.get_rect(topleft=(x, y))
        self.pos_x = float(x)
        self.pos_y = float(y)

    def handle_input(self, keys):

        dx = 0

        if keys[pygame.K_q]:
            dx = -PLAYER_SPEED
            self.direction = -1

        if keys[pygame.K_d]:
            dx = PLAYER_SPEED
            self.direction = 1

        self.pos_x += dx
        self.rect.x = int(self.pos_x)

        if self.direction == 1:
            self.image = self.initial_image

        elif self.direction == -1:
            self.image = pygame.transform.flip(self.initial_image, True, False)
        

    def jump(self):
        if self.on_ground:
            self.vel_y = JUMP_POWER
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

    def shoot(self):
        if self.shoot_cooldown <= 0:
            projectile = Projectile(
                self.rect.centerx,
                self.rect.centery,
                self.direction
            )

            self.projectiles.append(projectile)
            self.shoot_cooldown = 20

    def melee_attack(self):
        if self.attack_cooldown <= 0:
            self.attack_cooldown = 20

            if self.direction == 1:
                attack_rect = pygame.Rect(
                    self.rect.right,
                    self.rect.y,
                    40,
                    self.rect.height
                )
            else:
                attack_rect = pygame.Rect(
                    self.rect.left - 40,
                    self.rect.y,
                    40,
                    self.rect.height
                )

            return attack_rect

        return None

    def update(self):
        self.apply_gravity()

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        for projectile in self.projectiles:
            projectile.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for projectile in self.projectiles:
            projectile.draw(screen)