import pygame
import random
import math


class MonsterSpawner:
    def __init__(self, player, all_sprites, monsters):
        self.player = player
        self.all_sprites = all_sprites
        self.monsters = monsters
        self.spawn_delay = 1000  # 밀리초 단위로 몬스터 생성 지연 시간
        self.last_spawn_time = pygame.time.get_ticks()
        self.start_time = pygame.time.get_ticks()
        self.monster_classes = []  # 생성할 몬스터 클래스 리스트
        
    def add_monster_class(self, monster_class):
        self.monster_classes.append(monster_class)

    def spawn_monster(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) // 1000
        spawn_count = max(1, elapsed_time // 20 + 1)  # 20초마다 생성 개수 증가

        if current_time - self.last_spawn_time > self.spawn_delay:
            self.last_spawn_time = current_time
            for _ in range(spawn_count):
                if self.monster_classes:
                    monster_class = random.choice(self.monster_classes)
                    angle = random.uniform(0, 2 * math.pi)
                    distance = 700
                    x = self.player.rect.x + distance * math.cos(angle)
                    y = self.player.rect.y + distance * math.sin(angle)
                    monster = monster_class(x, y, self.player)
                    self.monsters.add(monster)
                    self.all_sprites.add(monster)
