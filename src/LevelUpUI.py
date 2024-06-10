import pygame
import random
from Button import Button

class LevelUpUI:
    def __init__(self, screen, level_up_image_path, game_instance):
        self.screen = screen
        self.level_up_image = pygame.image.load(level_up_image_path)
        self.level_up_image = pygame.transform.scale(self.level_up_image, (800, 600))
        self.rect = self.level_up_image.get_rect(center=(650, 400))
        self.active = False
        self.game_instance = game_instance

        self.button_width = 300
        self.button_height = 90
        self.item_button_x = self.rect.centerx - self.button_width // 2
        self.item_button_y = self.rect.centery - (self.button_height // 2) - 25

        # 아이템 이미지와 설명 추가 하는 곳
        self.item_images = {"./image/carrot.png" : "  당근을 쏠 수 있습니다." , 
                            "./image/appleItem.png" : "  사과 개수가 증가합니다.", 
                            "./image/grass.png" : "  나뭇잎이 사방으로 날라갑니다."
                            }
        # 상태 이미지와 설명 설명 추가 하는 곳
        self.status_images = {
            "./image/grass.png": "  추가 방어력 획득",
            "./image/carrot.png": "  생명력 증가",
            "./image/status.png": "  마법 능력 강화"
        }

        self.initialize_buttons()

    def initialize_buttons(self):
        # 랜덤 선택을 위해 이미지 경로와 텍스트를 직접 추출
        item_image_path, item_text = random.choice(list(self.item_images.items()))
        self.item_button = Button(
            self.item_button_x, self.item_button_y, self.button_width, self.button_height,
            self.resume_game, "./image/SelectItemSlot.png", [item_image_path], item_text
        )
        
        status_image_path, status_text = random.choice(list(self.status_images.items()))
        self.status_button = Button(
            self.item_button_x, self.item_button_y + self.button_height + 20, self.button_width, self.button_height,
            self.resume_game, "./image/SelectItemSlot.png", [status_image_path], status_text
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
        self.initialize_buttons()
        self.active = True