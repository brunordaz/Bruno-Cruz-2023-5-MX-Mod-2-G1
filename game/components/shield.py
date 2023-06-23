import pygame, random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD


class Shield(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(SHIELD, (50, 60))
        self.rect = self.image.get_rect()
        self.reset_position()
        self.speed = 8
        self.active = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_position()

    def reset_position(self):
        self.rect.y = random.randint(-self.rect.height, -10)
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
