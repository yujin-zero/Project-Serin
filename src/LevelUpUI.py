import pygame
import random
from Button import Button

class LevelUpUI:
    def __init__(self, screen, level_up_image_path, game_instance):
        self.screen = screen
        self.level_up_image = pygame.image.load(level_up_image_path)
        self.rect = self.level_up_image.get_rect(center=(650, 400))
        self.active = False
        self.game_instance = game_instance

        self.button_width = 200
        self.button_height = 60
        self.item_button_x = self.rect.centerx - self.button_width // 2
        self.item_button_y = self.rect.centery - (self.button_height // 2) - 25
        # 아이템 추가 넣는 곳
        self.item_images = ["./image/carrot.png", "./image/appleItem.png"]

        # 초기 버튼 설정; 실제 사용은 activate()에서
        self.initialize_buttons()

    def initialize_buttons(self):
        # 랜덤 아이템 선택을 위해 매번 새로운 Button 인스턴스 생성
        self.item_button = Button(
            self.item_button_x, self.item_button_y, self.button_width, self.button_height,
            self.resume_game, "./image/SelectItemSlot.png", self.item_images
        )
        # 상태 아이템 추가 넣는 곳
        self.status_images = []
        self.status_button = Button(
            self.item_button_x, self.item_button_y + self.button_height + 20, self.button_width, self.button_height,
            self.resume_game, "./image/SelectItemSlot.png", []
        )
        
        self.buttons = [self.item_button, self.status_button]

    def draw(self):
        if self.active:
            self.screen.blit(self.level_up_image, self.rect.topleft)
            for button in self.buttons:
                button.draw(self.screen)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def resume_game(self):
        self.active = False
        self.game_instance.paused = False

    def activate(self):
        self.initialize_buttons()  # 버튼을 재초기화하여 랜덤 이미지를 반영
        self.active = True