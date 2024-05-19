import pygame
import sys
import random
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1
        if keys[pygame.K_UP]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN]:
            self.rect.y += 1

# Player 객체 생성
player = Player(400, 300)
