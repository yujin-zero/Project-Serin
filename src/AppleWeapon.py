import pygame
import math


class Apple(pygame.sprite.Sprite):
    def __init__(self, serin, radius, speed, damage):
        super().__init__()
        self.serin = serin
        self.radius = radius
        self.speed = speed
        self.image = pygame.image.load("./image/apple.png").convert_alpha()
        self.rect = self.image.get_rect(center=self.serin.rect.center)
        self.angle = 0
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
        self.damage = [0, 10, 15, 20, 25, 30]
        self.level = 1
        self.maxLevel = 5
        self.radius = 80
        self.speed = 4
        self.apple = Apple(serin, self.radius, self.speed,
                           self.damage[self.level])
        self.all_sprite.add(self.apple)

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay[self.level]:
            self.last_shot = now
            if self.level < self.maxLevel:
                self.level += 1
                self.apple.damage = self.damage[self.level]

    def update(self):
        self.apple.update()

    def draw(self):
        self.apple.draw(self.screen, 0, 0)
