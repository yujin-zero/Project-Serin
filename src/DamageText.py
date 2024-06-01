import pygame


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, font_size=24, color=(255, 0, 0)):
        super().__init__()
        self.font = pygame.font.Font(None, font_size)
        self.image = self.font.render(str(damage), True, color)
        self.rect = self.image.get_rect(center=(x, y))
        self.lifetime = 30  # 텍스트가 화면에 표시될 프레임 수

    def update(self):
        self.lifetime -= 1
        self.rect.y -= 1  # 텍스트가 위로 올라가도록 함
        if self.lifetime <= 0:
            self.kill()
