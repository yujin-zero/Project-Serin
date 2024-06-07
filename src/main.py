import pygame
import sys
import time
from Background import Background
from Camera import Camera
from Serin import Serin
import spawn
import monster_squirrel
import monster_BamBoo  # 대나무 몬스터 모듈
import monster_Spirit  # 영혼 몬스터 모듈
from ui import Ui
from Inventory import Inventory
from AppleWeapon import AppleWeapon  # 사과무기
from DamageText import DamageText  # 데미지 표시
from Gem import Gem  # 경험치


class Main:
    def __init__(self):
        pygame.init()
        self.screen_width = 1300
        self.screen_height = 800
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("밤의 수호자 세린")

        self.background = Background("./image/background.png")
        self.boundary_width = self.background.width
        self.boundary_height = self.background.height

        serin_start_x = self.boundary_width // 2
        serin_start_y = self.boundary_height // 2
        self.serin = Serin(serin_start_x, serin_start_y,
                           self.boundary_width, self.boundary_height)

        self.camera = Camera(self.screen_width, self.screen_height)
        self.running = True

        self.monsters = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.gems = pygame.sprite.Group()
        self.monster_spawner = spawn.MonsterSpawner(
            self.serin, self.all_sprites, self.monsters)
        self.monster_spawner.add_monster_class(
            monster_squirrel.SquirrelMonster)
        self.monster_spawner.add_monster_class(
            monster_BamBoo.BamBooMonster)
        self.monster_spawner.add_monster_class(
            monster_Spirit.SpiritMonster)

        self.all_sprites.add(self.serin)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.start_time = time.time()

        self.exp = 0
        self.max_exp = 100
        self.monster_kills = 0
        self.kill_icon = pygame.image.load(
            "./image/monster_kill_icon.png").convert_alpha()
        self.coin_count = 0
        self.coin = pygame.image.load("./image/coin.png")
        self.inventory = Inventory()
        self.ui = Ui(self.inventory, self.screen)

        self.apple_weapon = AppleWeapon(
            self.serin, 100, 5, "./image/apple.png")
        self.damage_texts = pygame.sprite.Group()

        # test
        self.inventory.add_item(self.apple_weapon)

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self._check_collisions()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        self.serin.update()
        self.camera.update(self.serin)
        self.monster_spawner.spawn_monster()
        self.all_sprites.update()
        self.damage_texts.update()
        self.gems.update()
        if self.inventory.has_apple_weapon():
            self.apple_weapon.update()
        pygame.display.flip()
        self.clock.tick(60)

        if self.exp >= self.max_exp:
            self.exp = 0

    def _draw(self):
        self.background.draw(self.screen, self.camera.x, self.camera.y)
        for sprite in self.all_sprites:
            sprite.draw(self.screen, self.camera.x, self.camera.y)
        for gem in self.gems:
            gem.draw(self.screen, self.camera.x, self.camera.y)
        for damage_text in self.damage_texts:
            self.screen.blit(damage_text.image, (damage_text.rect.x -
                             self.camera.x, damage_text.rect.y - self.camera.y))
        if self.inventory.has_apple_weapon():
            self.apple_weapon.draw(self.screen, self.camera.x, self.camera.y)

        self._draw_clock()
        self._draw_exp_bar()
        self._draw_kill_count()
        self._draw_coin()
        self.ui.draw()

        pygame.display.flip()

    def _check_collisions(self):
        for monster in self.monsters:
            if self.serin.hitbox.colliderect(monster.hitbox):
                self.serin.health -= 0.1  # monster.power
                if self.serin.health <= 0:
                    self.serin.kill()
                    self.running = False

            if self.inventory.has_apple_weapon() and self.apple_weapon.rect.colliderect(monster.hitbox):
                damage = 10
                monster.health -= damage
                self.damage_texts.add(DamageText(
                    monster.rect.centerx, monster.rect.centery, damage))
                if monster.health <= 0:
                    monster.kill()
                    self.monster_kills += 1
                    self.coin_count += 1
                    gem = Gem(monster.rect.centerx, monster.rect.centery)
                    self.gems.add(gem)
                    self.all_sprites.add(gem)

        for gem in self.gems:
            if self.serin.hitbox.colliderect(gem.rect):
                self.exp += 10
                gem.kill()

    def _draw_clock(self):
        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        time_text = f"{minutes:02}:{seconds:02}"

        text_surface = self.font.render(time_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.screen_width // 2, 80))

        self.screen.blit(text_surface, text_rect)

    def _draw_exp_bar(self):
        bar_length = 1300
        bar_height = 20
        fill = (self.exp / self.max_exp) * bar_length
        outline_rect = pygame.Rect(
            (self.screen_width - bar_length) // 2, 10, bar_length, bar_height)
        fill_rect = pygame.Rect(
            (self.screen_width - bar_length) // 2, 10, fill, bar_height)

        pygame.draw.rect(self.screen, (255, 255, 0), fill_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), outline_rect, 2)

    def _draw_kill_count(self):
        kill_count_text = f"{self.monster_kills}"
        text_surface = self.font.render(kill_count_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(
            top=50, right=self.screen_width - 200)
        icon_rect = self.kill_icon.get_rect(
            top=45, left=text_rect.right + 10)

        self.screen.blit(self.kill_icon, icon_rect)
        self.screen.blit(text_surface, text_rect)

    def _draw_coin(self):
        coin_count_text = f"{self.coin_count}"
        text_surface = self.font.render(coin_count_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(
            top=50, right=self.screen_width - 100)

        icon_rect = self.coin.get_rect(top=29, left=text_rect.right-10)

        self.screen.blit(self.coin, icon_rect)
        self.screen.blit(text_surface, text_rect)


if __name__ == "__main__":
    Main().run()
