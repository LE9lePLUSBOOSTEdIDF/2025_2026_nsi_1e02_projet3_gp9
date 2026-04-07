import pygame 
pygame.init()

pygame.display.set_caption('popo')
screen= pygame.display.set_mode ((1920,1080)) 

backgroud = pygame.image.load('assets/background_castle.png')

running = True

while running : 
    
    screen.blit(backgroud,(0,0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
            pygame.quit() 
            print("fermeture du jeu") 

for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game_running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

            elif event.key == pygame.K_z:
                game.player.jump()
        
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start_game()