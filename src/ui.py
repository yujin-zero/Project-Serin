import pygame


class Ui:
    def __init__(self,  inventory, screen ):
        self.inventory = inventory
        self.screen = screen
        self.font = pygame.font.Font(None, 24)

    def draw(self):
        self.draw_inventory()

    def draw_inventory(self):
        x = 0
        y = 50
        image_size = 50

        for _ in range(4):
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (x, y, image_size, image_size), 2)
            x += image_size

        # 무기 아이템 그리기
        x = 0
        for weapon in self.inventory.weapon_list:
            if hasattr(weapon, 'image'):
                self.screen.blit(weapon.image, (x, y))
                level_text = self.font.render(
                    f"Lv{weapon.level}", True, (255, 255, 255))
                self.screen.blit(level_text, (x, y + image_size))
                x += image_size

        # 능력치 아이템 그리기
        x = 0
        y = 120
        for _ in range(4):
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (x, y, image_size, image_size), 2)
            x += image_size

        x = 0
        for item in self.inventory.item_list:
            if hasattr(item, 'image'):
                self.screen.blit(item.image, (x, y))
                level_text = self.font.render(
                    f"Lv{item.level}", True, (255, 255, 255))
                self.screen.blit(level_text, (x, y + image_size))
                x += image_size
        for item in self.inventory.item2_list:
            if hasattr(item, 'image'):
                self.screen.blit(item.image, (x, y))
                level_text = self.font.render(
                    f"Lv{item.level}", True, (255, 255, 255))
                self.screen.blit(level_text, (x, y + image_size))
                x += image_size
