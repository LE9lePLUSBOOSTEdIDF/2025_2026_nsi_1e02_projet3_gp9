import pygame
from player import Player

class Game(): # Création d'une classe générale pour le jeu
    
    def __init__(self):
        self.player = Player()
        self.pressed = {}