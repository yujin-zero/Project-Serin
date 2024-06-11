import pygame


class HealthBoostItem:
    def __init__(self):
        self.image = pygame.image.load("./image/health.png").convert_alpha()
        self.level = 5

    def update(self, Serin):
        if self.level < 5:
            Serin.max_health += 50
            self.level += 1
