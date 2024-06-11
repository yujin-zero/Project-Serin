import Serin
import pygame


class Ui:
    def __init__(self,  inventory, screen):
        self.inventory = inventory
        self.screen = screen
        self.font = pygame.font.Font(None, 24)

    def draw(self):
        self.draw_inventory()

    def draw_inventory(self):
        x = 0
        y = 50

        image_size = 50

        for i in range(4):
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (x, y, image_size, image_size), 2)
            x += image_size

        # 아이템 그리기
        x = 0
        for weapon in self.inventory.weapon_list:
            if hasattr(weapon, 'image'):
                self.screen.blit(weapon.image, (x, y))
                level_text = self.font.render(
                    f"Lv{weapon.level}", True, (255, 255, 255))
                self.screen.blit(level_text, (x, y + image_size))
                x += image_size
