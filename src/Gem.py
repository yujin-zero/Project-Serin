import pygame


class Gem(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path="./image/gem.png"):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        # 보석에 대한 업데이트 로직이 있으면 여기에 추가
        pass

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (self.rect.x -
                    camera_x, self.rect.y - camera_y))
