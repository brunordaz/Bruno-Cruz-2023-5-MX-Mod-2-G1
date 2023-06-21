import pygame, random

from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    def __init__(self, type):
        self.type = type
        self.width = 40
        self.height = 50
        self.images = random.choice[ENEMY_1, ENEMY_2]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH-self.width)
        self.rect.y = 0
        self.speed = 10
    
    def draw (self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def create_enemy(self):
        current_time = pygame.time.get_ticks()
        time_delay = random.randint(1000, 2000)

        if current_time - self.enemy_creation_time > time_delay:
            x_pos = random.randint(0, SCREEN_WIDTH - self.image_width)
            selected_image = random.choice(self.enemy_images)
            enemy_image = pygame.transform.scale(selected_image, (self.image_width, self.image_height))
            enemy = {
                'image': enemy_image,
                'rect': self.rect.copy(),
                'move_direction': random.choice(["left", "right"])
            }
            enemy['rect'].topleft = (x_pos, -self.image_height)
            self.enemies.append(enemy)
            self.timer = current_time


    def update(self):
        direction_change_delay = random.randint (500, 1000)
        for enemy in self.enemies:
            enemy['rect'].y += self.game_speed
            self.update_enemy_position(enemy)

            if enemy['rect'].top > SCREEN_HEIGHT:
                self.enemies.remove(enemy)
            else:
                current_time = pygame.time.get_ticks()

                if current_time - self.direction_change_timer > self.direction_change_delay:
                    new_direction = random.choice(["left", "right"])
                    if new_direction != enemy['move_direction']:
                        enemy['move_direction'] = new_direction
                    else:
                        enemy['move_direction'] = "left" if enemy['move_direction'] == "right" else "right"

                    self.direction_timer = current_time


    def update_enemy_position(self, enemy):
        if enemy['move_direction'] == "left":
            enemy['rect'].x -= self.game_speed
            if enemy['rect'].left < 0:
                enemy['move_direction'] = "right"
        elif enemy['move_direction'] == "right":
            enemy['rect'].x += self.game_speed
            if enemy['rect'].right > SCREEN_WIDTH:
                enemy['move_direction'] = "left"

    def draw(self, screen):
        for enemy in self.enemies:
            screen.blit(enemy['image'], enemy['rect'])

    def reset(self):
        x_pos = random.randint(0, SCREEN_WIDTH - self.image_width)
        y_pos = random.randint(-2 * self.image_height, -self.image_height)
        self.rect.topleft = (x_pos, y_pos)
        self.move_direction = random.choice(["left", "right"]) # Reiniciar el temporizador

    def update(self):
        for enemy in self.enemies:
            enemy['rect'].y += self.game_speed

            if enemy['rect'].top > SCREEN_HEIGHT:
                self.enemies.remove(enemy)
            else:
                current_time = pygame.time.get_ticks()

                if current_time - self.direction_timer > self.direction_change_delay:
                    new_direction = random.choice(["left", "right"])
                    if new_direction != enemy['move_direction']:
                        enemy['move_direction'] = new_direction
                    else:
                        enemy['move_direction'] = "left" if enemy['move_direction'] == "right" else "right"

                    self.direction_timer = current_time

                if enemy['move_direction'] == "left":
                    enemy['rect'].x -= self.game_speed
                    if enemy['rect'].left < 0:
                        enemy['move_direction'] = "right"
                elif enemy['move_direction'] == "right":
                    enemy['rect'].x += self.game_speed
                    if enemy['rect'].right > SCREEN_WIDTH:
                        enemy['move_direction'] = "left"

    def draw(self, screen):
        for enemy in self.enemies:
            screen.blit(enemy['image'], enemy['rect'])

    def reset(self):
        x_pos = random.randint(0, SCREEN_WIDTH - self.image_width)
        y_pos = random.randint(-2 * self.image_height, -self.image_height)
        self.rect.topleft = (x_pos, y_pos)
        self.move_direction = random.choice(["left", "right"])
