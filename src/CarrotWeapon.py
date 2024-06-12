import pygame
import random
import math
import time


class Carrot(pygame.sprite.Sprite):
    def __init__(self, damage, serin):
        super().__init__()
        self.image = pygame.image.load("./image/leaf.png").convert_alpha()

        self.speed = 14
        self.angle = random.uniform(0, 360)
        self.damage = damage
        self.rect = self.image.get_rect(center=serin.rect.center)
        self.creation_time = pygame.time.get_ticks()
        self.original_image = pygame.image.load(
            "./image/carrot.png").convert_alpha()  # 원본 이미지 저장
        self.image = self.original_image
        self.rotate_image()
        self.velocity_x = math.cos(math.radians(self.angle)) * self.speed
        self.velocity_y = math.sin(math.radians(self.angle)) * self.speed

    def rotate_image(self):
        # 이동 방향에 따라 이미지를 회전 (270도 추가 회전)
        self.image = pygame.transform.rotate(
            self.original_image, -self.angle + 155)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if (self.rect.right < 0 or self.rect.left > 3500 or
                self.rect.bottom < 0 or self.rect.top > 3500):
            self.kill()

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (self.rect.x -
                    camera_x, self.rect.y - camera_y))


class CarrotWeapon(pygame.sprite.Sprite):
    def __init__(self, serin, screen, weapon_sprite):
        super().__init__()
        self.serin = serin
        self.radius = 0
        self.speed = 10
        self.base_damage = 20
        self.damage = self.base_damage
        self.base_carrot_fire_interval = 1.0
        self.carrot_fire_interval = self.base_carrot_fire_interval
        self.last_carrot_fire_time = time.time()
        self.weapon_sprite = weapon_sprite
        self.screen = screen
        self.level = 1
        self.maxLevel = 5
        self.image = pygame.image.load("./image/carrot.png").convert_alpha()
        self.update_stats()

    def update_stats(self):
        self.damage = self.base_damage + 5 * (self.level - 1)
        self.carrot_fire_interval = self.base_carrot_fire_interval - \
            0.2 * (self.level - 1)

    def attack(self):
        current_time = time.time()
        if current_time - self.last_carrot_fire_time >= self.carrot_fire_interval:
            carrot = Carrot(self.damage, self.serin)
            self.weapon_sprite.add(carrot)
            self.last_carrot_fire_time = current_time

    def update(self):
        pass

    def draw(self):
        pass
