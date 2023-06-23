import pygame, random
from random import randint
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, SOUND, FONT_STYLE
from game.components.spaceship import Spaceship
from game.components.shield import Shield
from game.components.enemies.enemy import Enemy
from game.components.gameover import GameOverScreen


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.shield = Shield()
        self.enemies = []
        self.generate_enemies()
        self.sounds = SOUND
        self.game_over_screen = GameOverScreen(self.restart_game)
        self.score = 0
        self.deaths = 0
        self.max_score = 0
        self.font = pygame.font.Font(FONT_STYLE, 40)
        self.life = 0

    def run(self):
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.spaceship.fire_bullet()

    def update(self):
        events = pygame.key.get_pressed()
        self.spaceship.update(events)
        self.shield.update()
        for enemy in self.enemies:
            enemy.update()
            if randint(1, 20) == 1:
                enemy.fire_bullet()
        self.handle_collisions()
        if not self.enemies:
            self.generate_enemies()

    def handle_collisions(self):
        for bullet in self.spaceship.bullets:
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.spaceship.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.sounds.play()
                    self.score += 100
                    self.deaths += 1
        for enemy in self.enemies:
            for bullet in enemy.bullets:
                if bullet.rect.colliderect(self.spaceship.rect):
                    self.life -= 1
                    if self.life <= 0:
                        self.spaceship.normal()
                        self.game_over()
        if pygame.sprite.spritecollide(self.spaceship, self.enemies, False):
            self.life -= 1
            if self.life <= 0:
                self.spaceship.normal()
                self.game_over()
        if pygame.sprite.collide_rect(self.spaceship, self.shield):
            self.life += 1
            self.spaceship.shield_collision()
            self.shield.kill()

    def generate_enemies(self):
        for _ in range(5):
            enemy = Enemy()
            self.enemies.append(enemy)

    def game_over(self):
        self.playing = False
        self.max_score = max(self.score, self.max_score)
        self.game_over_screen.show(self.screen, self.score, self.max_score, self.deaths)
        self.score = 0
        self.deaths = 0
        self.spaceship.reset()
        self.enemies.clear()

    def restart_game(self):
        self.playing = True

    def draw(self):
        
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.spaceship.draw(self.screen)
        self.shield.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        self.draw_score()
        self.spaceship.draw_bullets(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)
        self.screen.blit(score_text, score_rect)

        life_text = self.font.render(f"Shield: {self.life}", True, (255, 255, 255))
        life_rect = life_text.get_rect()
        life_rect.topright = (self.screen.get_width() - 10, 10)
        self.screen.blit(life_text, life_rect)
