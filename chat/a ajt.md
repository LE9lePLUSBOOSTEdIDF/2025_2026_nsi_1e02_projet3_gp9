double saut
dash
boss
ennemis différents
système de score
checkpoints
animations
invincibilité ap

6. RECT D’ATTAQUE CORPS À CORPS

Dans player.py.

Ce rectangle est INVISIBLE.

Il sert juste à détecter les collisions.

attack_rect = pygame.Rect(
    self.rect.right,
    self.rect.y,
    40,
    self.rect.height
)

ou vers la gauche :

attack_rect = pygame.Rect(
    self.rect.left - 40,
    self.rect.y,
    40,
    self.rect.height
)
7. COLLISIONS
Joueur / plateformes

Dans level.py :

if player.rect.colliderect(platform):
Projectile / ennemi

Dans game.py :

if projectile.rect.colliderect(enemy.rect):
Ennemi / joueur
if enemy.rect.colliderect(self.player.rect):
8. FLIP DU SPRITE JOUEUR

Pour regarder à gauche/droite.

Dans draw() du joueur :

if self.direction == -1:
    flipped = pygame.transform.flip(
        self.image,
        True,
        False
    )

    screen.blit(flipped, self.rect)

else:
    screen.blit(self.image, self.rect)
9. HITBOX PLUS PETITE (TRÈS IMPORTANT)

Les sprites ont souvent du vide.

Donc on fait souvent une hitbox plus petite.

Exemple :

self.rect = pygame.Rect(x, y, 40, 70)

Même si le sprite fait :

(70, 90)

👉 Ça rend le gameplay BEAUCOUP plus propre.

10. DEBUG DES HITBOXES

Très utile pendant le développement.

Dans draw() :

pygame.draw.rect(
    screen,
    (255, 0, 0),
    self.rect,
    2
)

Le 2 signifie :

contour seulement
11. PLATEFORMES

Même logique.

Les plateformes peuvent rester des rectangles :

pygame.Rect(300, 500, 200, 30)

Puis affichées avec :

pygame.draw.rect(screen, GRAY, platform)

OU remplacées plus tard par des tiles.

12. STRUCTURE FINALE CONSEILLÉE
assets/
│
├── knight_sprite.png
├── monster_skeleton_knight.png
├── projectile.png
└── background_castle.png
13. Le pipeline complet d’un sprite dans Pygame

Toujours :

1. charger
pygame.image.load()
2. convertir
.convert_alpha()
3. resize
pygame.transform.scale()
4. créer le rect
get_rect()
5. afficher
screen.blit()
14. Exemple COMPLET joueur
self.image = pygame.image.load(
    "assets/knight_sprite.png"
).convert_alpha()

self.image = pygame.transform.scale(
    self.image,
    (70, 90)
)

self.rect = self.image.get_rect(
    topleft=(x, y)
)

Puis :

screen.blit(self.image, self.rect)
15. Ce qu’il vous manque ensuite pour un vrai rendu pro

Le gros gap de qualité vient après avec :

animations spritesheet
caméra qui suit le joueur
scrolling
tileset
particules
knockback
sons
animation d’attaque
animation de mort
états (idle, run, jump, attack)

C’est là qu’un projet étudiant commence à ressembler à un vrai jeu indie.