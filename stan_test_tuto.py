import pygame
pygame.init() # Charger tous les modules de la bibliothèque

# Création de la fenêtre

pygame.display.set_caption("Jeu de NSI") # Création du titre
main_screen = pygame.display.set_mode((1080, 720)) # Dimensions de la fenêtre

background = pygame.image.load("assets/background_castle.png") 

game_running = True # Création de la boucle pour faire tourner le jeu en continu

while game_running:

    main_screen.blit(background, (0, 0)) # Ajout de l'arrière plan à l'écran
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game_running = False
            pygame.quit()