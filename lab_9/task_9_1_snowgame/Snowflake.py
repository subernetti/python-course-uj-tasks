import pygame 
import random

class Snowflake(pygame.sprite.Sprite):
    # Inicjalizacja platka sniegu
    def __init__(self, x_pos):
        super().__init__()

        try:
            original_image = pygame.image.load("image_snowflake.png").convert_alpha()
            self.image = pygame.transform.scale(original_image, (40, 40))
        except FileNotFoundError:
            self.image = pygame.Surface((40,40))
            self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect(center=((x_pos, -20)))
        self.speed = random.randint(2, 5)

    # Aktualizacja pozycji platka sniegu
    def update(self):
        self.rect.y += self.speed