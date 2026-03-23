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