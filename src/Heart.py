import pygame


class Heart:
    def __init__(self):
        self.image = pygame.image.load("./image/heart.png").convert_alpha()
        self.level = 0

    def update(self, Serin):
        if self.level < 5:
            if Serin.health+20 > 50:
                Serin.health = 50
            else:
                Serin.health += 20
            self.level += 1
