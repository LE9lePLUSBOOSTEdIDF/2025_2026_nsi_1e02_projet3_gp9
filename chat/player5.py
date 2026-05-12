import pygame
        self.projectiles = []

        self.attack_cooldown = 0
        self.shoot_cooldown = 0

    def handle_input(self, keys):
        dx = 0

        if keys[pygame.K_q]:
            dx = -PLAYER_SPEED
            self.direction = -1

        if keys[pygame.K_d]:
            dx = PLAYER_SPEED
            self.direction = 1

        self.rect.x += dx

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
        pygame.draw.rect(screen, BLUE, self.rect)

        for projectile in self.projectiles:
            projectile.draw(screen)