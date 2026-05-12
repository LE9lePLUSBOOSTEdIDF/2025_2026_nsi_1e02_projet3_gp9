import pygame
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

        for projectile in self.player.projectiles:
            for enemy in self.enemies:
                if projectile.rect.colliderect(enemy.rect):
                    enemy.health -= projectile.damage

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
        self.screen.fill(DARK)

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