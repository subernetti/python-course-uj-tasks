import pygame
import sys
import random

from Snowflake import Snowflake

# Stale wartosci (w przyszlosci beda do wyboru)
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (20, 30, 200)

class Game:
    # Inicjalizacja parametrow gry
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The snow is falling down!")
        self.clock = pygame.time.Clock()

        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 36)

        self.Snowflakes = pygame.sprite.Group()
        self.score = 0
        self.game_over = False

        self.SPAWN_SNOW = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_SNOW, 800)

    # Uruchomienie calej gry
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    # Obsluga zdarzen (wyjscie, zrodzenie platkow, eliminacja platka)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not self.game_over:
                if event.type == self.SPAWN_SNOW:
                    random_x = random.randint(20, WIDTH - 20)
                    new_snowflake = Snowflake(random_x)
                    self.Snowflakes.add(new_snowflake)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for snowflake in self.Snowflakes:
                        if snowflake.rect.collidepoint(mouse_pos):
                            snowflake.kill()
                            self.score += 1
                            break

    # Aktualizacja stanu platkow sniegu
    def update(self):
        if not self.game_over:
            self.Snowflakes.update()
        
            for snowflake in self.Snowflakes:
                if snowflake.rect.bottom >= HEIGHT:
                    self.game_over = True

    # Wyswietlenie ekranu gry
    def draw(self):
        self.screen.fill(BG_COLOR)

        self.Snowflakes.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            go_text = self.font.render(f"GAME OVER! Your Score: {self.score}", True, (255, 50, 50))
            text_rect = go_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            self.screen.blit(go_text, text_rect)

        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()