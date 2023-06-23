import pygame
import sys
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE


class GameOverScreen:
    def __init__(self, restart_game):
        self.restart_game = restart_game
        self.font = pygame.font.Font(FONT_STYLE, 50)
        self.font_2 = pygame.font.Font(FONT_STYLE, 30)
        self.game_over_text = None
        self.instruction = None
        self.score_text = None
        self.deaths_text = None
        self.max_score_text = None

    def show(self, screen, score, max_score, deaths):
        screen.fill((0, 0, 0))
        self.render_texts(score, max_score, deaths)
        self.draw_texts(screen)
        pygame.display.flip()
        self.wait_for_input()

    def render_texts(self, score, max_score, deaths):
        self.game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.instruction = self.font_2.render("Press any key to continue", True, (255, 255, 255))
        self.score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.max_score_text = self.font.render(f"Max Score: {max_score}", True, (255, 255, 255))
        self.deaths_text = self.font.render(f"Deaths: {deaths}", True, (255, 255, 255))

    def draw_texts(self, screen):
        screen.blit(self.game_over_text, (SCREEN_WIDTH // 2 - self.game_over_text.get_width() // 2, SCREEN_HEIGHT // 4 - 50))
        screen.blit(self.instruction, (SCREEN_WIDTH // 2 - self.instruction.get_width() // 2, SCREEN_HEIGHT // 2.5 - 50))
        screen.blit(self.score_text, (SCREEN_WIDTH // 2 - self.score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(self.max_score_text, (SCREEN_WIDTH // 2 - self.max_score_text.get_width() // 2, SCREEN_HEIGHT // 1.65 + 50))
        screen.blit(self.deaths_text, (SCREEN_WIDTH // 2 - self.deaths_text.get_width() // 2, SCREEN_HEIGHT // 1.25 + 50))

    def wait_for_input(self):
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.restart_game()
                    wait = False
