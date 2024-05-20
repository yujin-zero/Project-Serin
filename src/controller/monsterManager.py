import pygame
import sys
import random
import math
import object.enemy
from object.enemy.monster_squirrel import SquirrelMonster
import object.player.player

class MonsterManager:
    def __init__(self, player, game_object,screen, camera):
        self.player = player
        self.game_object = game_object
        self.spawn_delay = 3000  # 밀리초 단위로 몬스터 생성 지연 시간
        self.last_spawn_time = pygame.time.get_ticks()
        self.start_time = pygame.time.get_ticks()
        self.monster_classes = []  # 생성할 몬스터 클래스 리스트
        self.add_monster_class(SquirrelMonster)
        self.screen = screen
        self.camera = camera

    def add_monster_class(self, monster_class):
        self.monster_classes.append(monster_class)

    def spawn_monster(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) // 1000  # 경과 시간을 초 단위로 변환
        spawn_count = max(1, elapsed_time // 10 + 1)  # 10초마다 생성 개수 증가
        self.game_object.update(self.camera)

        if current_time - self.last_spawn_time > self.spawn_delay:
            self.last_spawn_time = current_time
            for _ in range(spawn_count):
                if self.monster_classes:
                    monster_class = random.choice(self.monster_classes)
                    angle = random.uniform(0, 2 * math.pi)
                    distance = 400
                    x = self.player.rect.x + distance * math.cos(angle)
                    y = self.player.rect.y + distance * math.sin(angle)
                    monster = monster_class(x, y,self.player)
                    self.game_object.add(monster)
    
    def draw_monster(self):
        self.game_object.draw(self.screen)
    