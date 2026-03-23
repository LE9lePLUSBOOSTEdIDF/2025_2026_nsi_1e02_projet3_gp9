import pygame
pygame.init() # Charger tous les modules de la bibliothèque

class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 10

# Création de la fenêtre

pygame.display.set_caption("Jeu de NSI") # Création du titre
main_screen = pygame.display.set_mode((1080, 720)) # Dimensions de la fenêtre

background = pygame.image.load("assets/background_castle.png") 
background = pygame.transform.scale(background, (1080, 720))

game_running = True # Création de la boucle pour faire tourner le jeu en continu

while game_running:

    main_screen.blit(background, (0, 50)) # Ajout de l'arrière plan à l'écran
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game_running = False
            pygame.quit()

Episode 2