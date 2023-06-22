import pygame
from game.spaceship import spaceship

class shoting:
    
    def __init__(self) -> None:
           self.spaceship = spaceship() 
    
    def shoot(self, keyboard_event):
        if keyboard_event[pygame.K_SPACE] == True:
            self.spaceship.shoot()

        elif keyboard_event[pygame.K_SPACE] == False:
             pass
