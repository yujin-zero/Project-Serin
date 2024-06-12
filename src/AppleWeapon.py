import pygame
import math


class Apple(pygame.sprite.Sprite):
    def __init__(self, serin, radius, speed, damage, angle_offset):
        super().__init__()
        self.serin = serin
        self.radius = radius
        self.speed = speed
        self.image = pygame.image.load("./image/apple.png").convert_alpha()
        self.rect = self.image.get_rect(center=self.serin.rect.center)
        self.angle = angle_offset
        self.damage = damage

    def update(self):
        self.angle += self.speed
        if self.angle >= 360:
            self.angle -= 360

        rad = math.radians(self.angle)
        self.rect.centerx = self.serin.rect.centerx + \
            int(self.radius * math.cos(rad))
        self.rect.centery = self.serin.rect.centery + \
            int(self.radius * math.sin(rad))

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (self.rect.x -
                    camera_x, self.rect.y - camera_y))


class AppleWeapon:
    def __init__(self, serin, screen, all_sprite):
        self.serin = serin
        self.screen = screen
        self.all_sprite = all_sprite
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = [0, 1000, 900, 800, 700, 600]
        self.damage = [0, 20, 20, 25, 25, 30]
        self.level = 1
        self.maxLevel = 5
        self.radius = 80
        self.speed = 4
        self.apples = []
        self.image = pygame.image.load("./image/apple.png").convert_alpha()
        self.add_apples()

    def add_apples(self):
        for apple in self.apples:
            apple.kill()  # 기존 사과 제거
        self.apples = []

        total_apples = self.level  # 레벨에 따른 사과 개수
        angle_step = 360 / total_apples

        for i in range(total_apples):
            angle_offset = i * angle_step
            apple = Apple(self.serin, self.radius, self.speed,
                          self.damage[self.level], angle_offset)
            self.apples.append(apple)
            self.all_sprite.add(apple)

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay[self.level]:
            self.last_shot = now

    def update(self):
        for apple in self.apples:
            apple.update()

    def draw(self):
        for apple in self.apples:
            apple.draw(self.screen, 0, 0)
