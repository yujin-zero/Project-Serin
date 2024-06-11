import pygame


class DamageReductionItem:
    def __init__(self):
        self.image = pygame.image.load("./image/armor.png").convert_alpha()
        self.level = 5

    def update(self, Serin):
        if Serin.health + self.level*3 > Serin.max_health:
            Serin.health = Serin.max_health
        else:
            Serin.health += self.level*3
