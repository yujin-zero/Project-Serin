import pygame
import math


class AppleWeapon(pygame.sprite.Sprite):
    def __init__(self, serin, radius, speed, image_path):
        super().__init__()
        self.serin = serin
        self.radius = radius
        self.speed = speed
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=self.serin.rect.center)
        self.angle = 0

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
