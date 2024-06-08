import pygame
import math
import random

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class Leaf(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, GREEN, [(5, 0), (10, 5), (5, 10), (0, 5)])  # Simple leaf shape
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = angle
        self.speed = 5
        self.creation_time = pygame.time.get_ticks()


    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)

        #2초가 지나면 삭제
        if pygame.time.get_ticks() - self.creation_time > 2000:
            self.kill()

# Leaf class
class LeafWeapon:
    def __init__(self, serin, screen):
        self.serin = serin
        self.screen = screen
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = {1000,900,900,800,700}
        self.angle = {180,180,90,90,45}
        self.level = 0;
        self.maxLevel = 5;

    def attack(self, all_sprites, leaves):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay[self.level]:
            self.last_shot = now
            for angle in range(0, 360, self.angle[self.level]):  
                rad_angle = math.radians(angle)
                leaf = Leaf(self.serin.rect.centerx, self.serin.rect.centery, rad_angle)
                all_sprites.add(leaf)
                leaves.add(leaf)
        
