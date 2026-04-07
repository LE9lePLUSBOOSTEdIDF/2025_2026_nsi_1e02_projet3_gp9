import pygame
from game import Game
from projectile import Projectile

pygame.init() # Charger tous les modules de la bibliothèque

# Création de la fenêtre

pygame.display.set_caption("Jeu de NSI") # Création du titre
main_screen = pygame.display.set_mode((1080, 720)) # Dimensions de la fenêtre

background = pygame.image.load("assets/background_castle.png")  # Chargement de l'arrière plan
background = pygame.transform.scale(background, (1080, 720))

banner = pygame.transform.scale_by(pygame.image.load("assets/goofyahh_banner.png"), 0.4)
banner_rect = banner.get_rect()
banner_rect_x = 1080 / 5
banner_rect_y = 720 / 5

plateform = pygame.transform.scale(pygame.image.load("assets/plateform.png"), (200, 100))
plateform_rect = plateform.get_rect()
plateform_rect_x = 400
plateform_rect_y = 15

play_button = pygame.transform.scale_by(pygame.image.load("assets/play_button.png"), 0.4)
play_button_rect = play_button.get_rect()
play_button_rect.x = 1080 / 5
play_button_rect.y = 1080 / 5 + 200

game_over_banner = pygame.transform.scale_by(pygame.image.load("assets/game_over_banner.png"), 0.4)

game = Game()
game_running = True # Création de la boucle pour faire tourner le jeu en continu

while game_running:

    main_screen.blit(background, (0, 0)) # Affichage l'arrière plan à l'écran
    
    if game.is_running:
        #main_screen.blit(background, (1080, 720))
        game.update(main_screen, background)

    elif game.is_over:
        main_screen.blit(game_over_banner, (banner_rect_x, banner_rect_y))
        main_screen.blit(play_button, (play_button_rect.x, play_button_rect.y))

    else:
        main_screen.blit(banner, (banner_rect_x, banner_rect_y))
        main_screen.blit(play_button, (play_button_rect.x, play_button_rect.y))

    pygame.display.flip() # Actualisation de l'écran

