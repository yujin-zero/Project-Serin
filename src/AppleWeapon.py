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
        self.level = 1
        self.apples = []
        self._update_apples()

    def _update_apples(self):
        """사과 개수와 각도를 업데이트합니다."""
        self.apples = []
        angle_gap = 360 / self.level
        for i in range(self.level):
            apple_angle = self.angle + i * angle_gap
            self.apples.append({
                'angle': apple_angle,
                'rect': self.image.get_rect(center=self.serin.rect.center)
            })

    def set_level(self, level):
        """레벨을 설정하고 사과를 업데이트합니다."""
        self.level = level
        self._update_apples()

    def update(self):
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
