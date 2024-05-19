import pygame
import sys
import random
import math

# 초기화
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Window")
idx=0
# 색상 정의
bg_color = (230, 230, 230)  # RGB로 배경색 설정

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1
        if keys[pygame.K_UP]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN]:
            self.rect.y += 1
            
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, health, speed, power, image_paths, size=(30, 30)):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(img).convert_alpha(), size) for img in image_paths]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = health
        self.speed = speed
        self.power = power
        self.float_x = float(self.rect.x)
        self.float_y = float(self.rect.y)
        self.animation_index = 0
        self.animation_time = pygame.time.get_ticks()
        self.animation_delay = 100  # 밀리초 단위로 애니메이션 지연 시간 설정
        
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_time > self.animation_delay:
            self.animation_time = current_time
            self.animation_index = (self.animation_index + 1) % len(self.images)
            self.image = self.images[self.animation_index]

        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y
        dist = (dx**2 + dy**2)**0.5
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
        self.float_x += dx * self.speed
        self.float_y += dy * self.speed
        self.rect.x = int(self.float_x)
        self.rect.y = int(self.float_y)
        if self.health <= 0:
            self.kill()

class SquirrelMonster(Monster):
    def __init__(self, x, y):
        image_paths = [f"./10 - Enemies/graphics/monsters/raccoon/move/{i}.png" for i in range(5)]
        super().__init__(x, y, health=80, speed=0.2, power=5, image_paths=image_paths, size=(50, 50))

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
        elapsed_time = (current_time - self.start_time) // 1000  # 경과 시간을 초 단위로 변환
        spawn_count = max(1, elapsed_time // 10 + 1)  # 10초마다 생성 개수 증가

        if current_time - self.last_spawn_time > self.spawn_delay:#10초가 지나면
            self.last_spawn_time = current_time#시간 업데이트
            for _ in range(spawn_count):
                if self.monster_classes:
                    monster_class = random.choice(self.monster_classes)
                    angle = random.uniform(0, 2 * math.pi)
                    distance = 400
                    x = self.player.rect.x + distance * math.cos(angle)
                    y = self.player.rect.y + distance * math.sin(angle)
                    monster = monster_class(x, y)
                    self.monsters.add(monster)
                    self.all_sprites.add(monster)

# Player 객체 생성
player = Player(400, 300)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
monsters = pygame.sprite.Group()

# MonsterSpawner 객체 생성
monster_spawner = MonsterSpawner(player, all_sprites, monsters)
monster_spawner.add_monster_class(SquirrelMonster)
# 다른 몬스터 클래스도 추가할 수 있음
# monster_spawner.add_monster_class(OtherMonsterClass)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites.update()
    monster_spawner.spawn_monster()

    # 배경색 채우기
    screen.fill(bg_color)
    all_sprites.draw(screen)

    # 화면 업데이트
    pygame.display.flip()
