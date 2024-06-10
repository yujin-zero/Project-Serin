import pygame
import random
import math


class CarrotWeapon(pygame.sprite.Sprite):
    def __init__(self, serin, radius, speed, image_path, damage):
        super().__init__()
        self.serin = serin
        self.radius = radius
        self.speed = speed
        self.original_image = pygame.image.load(
            image_path).convert_alpha()  # 원본 이미지 저장
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.serin.rect.center)
        self.damage = damage
        self.angle = random.uniform(0, 360)  # 랜덤한 각도 설정
        self.velocity_x = math.cos(math.radians(self.angle)) * self.speed
        self.velocity_y = math.sin(math.radians(self.angle)) * self.speed
        self.rotate_image()

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
