import pygame
from game import Game

pygame.init() # Charger tous les modules de la bibliothèque

# Création de la fenêtre

pygame.display.set_caption("Jeu de NSI") # Création du titre
main_screen = pygame.display.set_mode((1080, 720)) # Dimensions de la fenêtre

background = pygame.image.load("assets/background_castle.png")  # Chargement de l'arrière plan
background = pygame.transform.scale(background, (1080, 720))

game = Game()
game_running = True # Création de la boucle pour faire tourner le jeu en continu

while game_running:

    main_screen.blit(background, (0, 0)) # Affichage l'arrière plan à l'écran
    main_screen.blit(game.player.image, game.player.rect) # Affichage du sprite 
    
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < main_screen.get_width():
        game.player.move_right()

    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()        

    pygame.display.flip() # Actualisation de l'écran

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game_running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

#Episode 2 : 25:00