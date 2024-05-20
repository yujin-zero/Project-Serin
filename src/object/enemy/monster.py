import pygame
import sys
import random
import math

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, player, health, speed, power, image_path, size=(30, 30)):
        super().__init__()
        self.player=player
        self.images = [pygame.transform.scale(pygame.image.load(img).convert_alpha(), size) for img in image_path]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = health
        self.speed = speed
        self.power = power
        self.animation_index = 0
        self.animation_time = pygame.time.get_ticks()
        self.animation_delay = 300  # 밀리초 단위로 애니메이션 지연 시간 설정
        
    def update(self,camera):
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_time > self.animation_delay:
            self.animation_time = current_time
            self.animation_index = (self.animation_index + 1) % len(self.images)
            self.image = self.images[self.animation_index]

        monster_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(self.player.rect.center) 
        camera_vector = pygame.math.Vector2(camera.camera_rect.center)

        distance = (player_vector - monster_vector - camera_vector).magnitude()

        if distance > 0:
            direction = (player_vector - monster_vector).normalize()
            self.rect.x += direction[0] * self.speed
            self.rect.y += direction[1] * self.speed

        if self.health <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
