import pygame, random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_ENEMY

class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.images = [ENEMY_1, ENEMY_2]
        self.image = pygame.transform.scale(random.choice(self.images), (50, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-self.rect.height, -10)
        self.speed_x = random.randint(-9, 9)
        self.speed_y = random.randint(8, 15)
        self.bullets = pygame.sprite.Group()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.bullets.draw(screen)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Verificar si el enemigo ha salido de la pantalla
        if self.rect.y > SCREEN_HEIGHT:
            self.reset_position()
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.change_direction()
        self.bullets.update()

    def reset_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-self.rect.height, -10)
        self.speed_x = random.randint(-9, 9)
        self.speed_y = random.randint(9, 29)
        self.image = pygame.transform.scale(random.choice(self.images), (50, 60))

    def change_direction(self):
        self.speed_x = -self.speed_x

    def fire_bullet(self):
        bullet = BulletEnemy(self.rect.centerx, self.rect.bottom)
        self.bullets.add(bullet)

class BulletEnemy(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(BULLET_ENEMY, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_y = 16

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
