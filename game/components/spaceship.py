import pygame
from pygame.sprite import Sprite
from game.components.shield import Shield
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET, SPACESHIP_SHIELD


class Bullet(Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.transform.scale(BULLET, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        self.rect.y -= 8


class Spaceship(Sprite):
    def __init__(self):
        super().__init__()
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (50, 60))
        self.rect = self.image.get_rect()
        self.speed = 8
        self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.bullets = []
        self.shield = Shield()
        self.shield_active = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            screen.blit(bullet.image, bullet.rect)

    def move_left(self, keyboard_events):
        if keyboard_events[pygame.K_LEFT]:
            self.rect.x -= self.speed

    def move_right(self, keyboard_events):
        if keyboard_events[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def move_up(self, keyboard_events):
        if keyboard_events[pygame.K_UP]:
            self.rect.y -= self.speed

    def move_down(self, keyboard_events):
        if keyboard_events[pygame.K_DOWN]:
            self.rect.y += self.speed

    def fire_bullet(self):
        bullet = Bullet((self.rect.x + self.rect.width // 2, self.rect.y))
        self.bullets.append(bullet)

    def reset(self):
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0
        self.bullets.clear()

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)

    def update(self, keyboard_events):
        self.move_up(keyboard_events)
        self.move_down(keyboard_events)
        self.move_left(keyboard_events)
        self.move_right(keyboard_events)
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
        self.update_bullets()

    def shield_collision(self):
        self.image = pygame.transform.scale(SPACESHIP_SHIELD, (50, 60))
        self.shield.kill()

    def normal(self):
        self.image = pygame.transform.scale(SPACESHIP, (50, 60))
