import pygame
import sys
import random
import math
import players

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, health, speed, power, image_paths,player, size=(30, 30)):
        super().__init__()
        self.player=player
        self.images = [pygame.transform.scale(pygame.image.load(img).convert_alpha(), size) for img in image_paths]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = health
        self.speed = speed
        self.power = power
        self.float_x = float(self.rect.x)
        self.float_y = float(self.rect.y)
        self.animation_index = 0
        self.animation_time = pygame.time.get_ticks()
        self.animation_delay = 100  # 밀리초 단위로 애니메이션 지연 시간 설정
        
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_time > self.animation_delay:
            self.animation_time = current_time
            self.animation_index = (self.animation_index + 1) % len(self.images)
            self.image = self.images[self.animation_index]

        dx = self.player.rect.x - self.rect.x
        dy = self.player.rect.y - self.rect.y
        dist = (dx**2 + dy**2)**0.5
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
        self.float_x += dx * self.speed
        self.float_y += dy * self.speed
        self.rect.x = int(self.float_x)
        self.rect.y = int(self.float_y)
        if self.health <= 0:
            self.kill()
