import pygame
import sys
from Background import Background  # 배경 이미지를 다루는 모듈
from Camera import Camera  # 카메라 모듈
from Serin import Serin  # 플레이어 캐릭터 모듈
import spawn  # 몬스터 스폰 모듈
import monster_squirrel  # 다람쥐 몬스터 모듈
import monster_BamBoo  # 대나무 몬스터 모듈
import monster_Spirit  # 영혼 몬스터 모듈

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

        # 세린을 맵의 정 가운데에 배치
        serin_start_x = self.boundary_width // 2
        serin_start_y = self.boundary_height // 2
        self.serin = Serin(serin_start_x, serin_start_y,
                           self.boundary_width, self.boundary_height)

        self.clock = pygame.time.Clock()
        self.camera = Camera(self.screen_width, self.screen_height)
        self.running = True

        self.monsters = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.monster_spawner = spawn.MonsterSpawner(
            self.serin, self.all_sprites, self.monsters)
        self.monster_spawner.add_monster_class(
            monster_squirrel.SquirrelMonster)
        self.monster_spawner.add_monster_class(
            monster_BamBoo.BamBooMonster)
        self.monster_spawner.add_monster_class(
            monster_Spirit.SpiritMonster)

        # Serin을 전체 스프라이트 그룹에 추가
        self.all_sprites.add(self.serin)

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

    def _draw(self):
        self.background.draw(self.screen, self.camera.x, self.camera.y)
        for sprite in self.all_sprites:
            sprite.draw(self.screen, self.camera.x, self.camera.y)
        pygame.display.flip()

    def _check_collisions(self):
         for monster in self.monsters:
            if self.serin.hitbox.colliderect(monster.hitbox):
                self.serin.health -= 0.1#monster.power  # 몬스터의 공격력에 따라 체력 감소
                if self.serin.health <= 0:
                    self.serin.kill()
                    #self.running=False
                
if __name__ == "__main__":
    Main().run()
