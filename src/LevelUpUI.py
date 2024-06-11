import pygame
import random
from Button import Button
from Inventory import Inventory


class LevelUpUI:
    def __init__(self, screen, level_up_image_path, game_instance):
        self.screen = screen
        self.level_up_image = pygame.image.load(level_up_image_path)
        self.level_up_image = pygame.transform.scale(
            self.level_up_image, (800, 600))
        self.rect = self.level_up_image.get_rect(center=(650, 400))
        self.active = False
        self.game_instance = game_instance

        self.button_width = 300
        self.button_height = 90
        self.item_button_x = self.rect.centerx - self.button_width // 2
        self.item_button_y = self.rect.centery - (self.button_height // 2) - 25

        # 아이템 이미지와 설명 추가 하는 곳
        self.item_images = {"./image/carrot.png": "  당근을 쏠 수 있습니다.",
                            "./image/appleItem.png": "  사과 개수가 증가합니다.",
                            "./image/grass.png": "  나뭇잎이 사방으로 날라갑니다."
                            }
        # 상태 이미지와 설명 설명 추가 하는 곳
        self.status_images = {
            "./image/armor.png": "  피해량 감소",
            "./image/health.png": "  최대 체력 증가",
            "./image/status.png": "  이동 속도 증가"
        }

        self.initialize_buttons()

    def initialize_buttons(self):
        # 랜덤 선택을 위해 이미지 경로와 텍스트를 직접 추출
        item_image_path, item_text = random.choice(
            list(self.item_images.items()))
        self.item_button = Button(
            self.item_button_x, self.item_button_y, self.button_width, self.button_height,
            lambda path=item_image_path: self.resume_game(
                path), "./image/SelectItemSlot.png", [item_image_path], item_text
        )

        status_image_path, status_text = random.choice(
            list(self.status_images.items()))
        self.status_button = Button(
            self.item_button_x, self.item_button_y + self.button_height +
            20, self.button_width, self.button_height,
            lambda path=status_image_path: self.resume_game(
                path), "./image/SelectItemSlot.png", [status_image_path], status_text

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

    def resume_game(self, item_image_path):

        if item_image_path == "./image/appleItem.png":
            print("사과 버튼이 눌렸습니다.")
            self.game_instance.inventory.increase_apple_weapon_level()
        elif item_image_path == "./image/carrot.png":
            print("당근 버튼이 눌렸습니다.")
            if self.game_instance.inventory.has_carrot_weapon():
                if self.game_instance.inventory.carrot_weapon.level < 5:
                    self.game_instance.inventory.carrot_weapon.level += 1
                    self.game_instance.inventory.carrot_weapon.carrot_fire_interval -= 0.15
            else:
                self.game_instance.inventory.add_weapon(
                    self.game_instance.inventory.carrot_weapon)
        elif item_image_path == "./image/grass.png":
            print("풀 버튼이 눌렸습니다.")
            if self.game_instance.inventory.has_leaf_weapon():
                if self.game_instance.inventory.leaf_weapon.level < 5:
                    self.game_instance.inventory.leaf_weapon.level += 1
            else:
                self.game_instance.inventory.add_weapon(
                    self.game_instance.inventory.leaf_weapon)
        elif item_image_path == "./image/armor.png":
            print("갑옷 버튼이 눌렸습니다.")
        elif item_image_path == "./image/health.png":
            print("체력 버튼이 눌렸습니다.")
        elif item_image_path == "./image/status.png":
            print("어쩌구")

        self.active = False
        self.game_instance.paused = False

    def activate(self):
        self.initialize_buttons()
        self.active = True
