import pygame

class Screen():

    def __init__(self, game):
        self.width = 1080
        self.height = 720
        self.game = game
        self.background = pygame.transform.scale(pygame.image.load("assets/background_castle.png"), (1080, 720))

    def create_screen(self):
        title = pygame.display.set_caption("Jeu de NSI")
        screen = pygame.display.set_mode(self.width, self.height)
        background = screen.blit(self.background, (1080, 720))

    def update():
        si le joueur est mort:
        
        quand le jeu débute
        faire spawn les monstres
        faire spawn le joueur

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

pygame.display.set_caption("Jeu de NSI") # Création du titre
main_screen = pygame.display.set_mode((1080, 720)) # Dimensions de la fenêtre

background = pygame.image.load("assets/background_castle.png")  # Chargement de l'arrière plan
background = pygame.transform.scale(background, (1080, 720))
