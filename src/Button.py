import pygame
import random

class Button:
    def __init__(self, x, y, w, h, callback, background_image_path, item_images, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.callback = callback
        self.font = pygame.font.SysFont("malgungothic", 17)
        self.background_image = pygame.image.load(background_image_path)
        self.background_image = pygame.transform.scale(self.background_image, (w, h))
        
        self.item_image = None
        self.text = text  # 기본 텍스트 설정

        # item_images가 비어 있지 않고, 리스트인지 확인
        if item_images and isinstance(item_images, list):
            selected_item_image_path = random.choice(item_images)
            self.item_image = pygame.image.load(selected_item_image_path)
            self.item_image = pygame.transform.scale(self.item_image, (50, 50))
            self.item_image_rect = self.item_image.get_rect(midleft=(self.rect.left + 10, self.rect.centery))
        else:
            self.text = ""  # 아이템 리스트가 비어있거나 잘못된 타입일 경우의 텍스트

        self.text_surf = self.font.render(self.text, True, pygame.Color('white'))
        self.text_rect = self.text_surf.get_rect(midleft=(self.rect.left + 60, self.rect.centery))

    def draw(self, screen):
        screen.blit(self.background_image, self.rect)
        if self.item_image:
            screen.blit(self.item_image, self.item_image_rect)
        screen.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
