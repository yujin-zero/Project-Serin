import pygame
import math


class AppleWeapon(pygame.sprite.Sprite):
    def __init__(self, serin):
        super().__init__()
        self.serin = serin
        self.radius = 100
        self.speed = 5
        self.image = pygame.image.load("./image/apple.png").convert_alpha()
        self.rect = self.image.get_rect(center=self.serin.rect.center)
        self.angle = 0
        self.level = 1
        self.apples = []

    def update(self):
        self.apples = []
        angle_gap = 360 / self.level
        for i in range(self.level):
            apple_angle = self.angle + i * angle_gap
            self.apples.append({
                'angle': apple_angle,
                'rect': self.image.get_rect(center=self.serin.rect.center)
            })

        self.angle += self.speed
        if self.angle >= 360:
            self.angle -= 360

        for apple in self.apples:
            apple['angle'] += self.speed
            if apple['angle'] >= 360:
                apple['angle'] -= 360

            rad = math.radians(apple['angle'])
            apple['rect'].centerx = self.serin.rect.centerx + \
                int(self.radius * math.cos(rad))
            apple['rect'].centery = self.serin.rect.centery + \
                int(self.radius * math.sin(rad))

    def draw(self, screen, camera_x, camera_y):
        for apple in self.apples:
            screen.blit(
                self.image, (apple['rect'].x - camera_x, apple['rect'].y - camera_y))
    
    def attack(self):
        pass