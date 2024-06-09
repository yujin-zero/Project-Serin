import pygame
import random


class Button:
    def __init__(self, x, y, w, h, callback, background_image_path, item_images):
        self.rect = pygame.Rect(x, y, w, h)
        self.callback = callback
        # 폰트 바꿔줄 착한 사람 구해요~
        # self.font = pygame.font.SysFont("malgungothic", 17)
        # self.font = pygame.font.SysFont("arial", 17)
        # self.font = pygame.font.SysFont("Arial Unicode MS", 17)
        # Noto Sans CJK 폰트 파일 직접 로드
        self.font = pygame.font.Font("NotoSansKR-Regular.ttf", 17)

        # 배경 이미지 로드 및 스케일 조정
        self.background_image = pygame.image.load(background_image_path)
        self.background_image = pygame.transform.scale(
            self.background_image, (w, h))

        # 아이템 이미지 랜덤 선택 및 로드
        if item_images:
            selected_item_image_path = random.choice(item_images)
            self.item_image = pygame.image.load(selected_item_image_path)
            self.item_image = pygame.transform.scale(self.item_image, (50, 50))
            self.item_image_rect = self.item_image.get_rect(
                midleft=(self.rect.left + 10, self.rect.centery))

            # 이미지에 따라 다른 텍스트 설정
            if "appleItem" in selected_item_image_path:
                self.text = "사과 개수 증가"
            elif "carrot" in selected_item_image_path:
                self.text = "당근 쏘기"
        else:
            self.item_image = None
            self.text = ""

        self.text_surf = self.font.render(
            self.text, True, pygame.Color('white'))
        self.text_rect = self.text_surf.get_rect(
            midleft=(self.rect.left + 60, self.rect.centery))

    def draw(self, screen):
        screen.blit(self.background_image, self.rect)
        if self.item_image:
            screen.blit(self.item_image, self.item_image_rect)
        screen.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()  # 버튼 클릭 시 콜백 함수 실행
