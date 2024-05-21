import pygame
import sys
import spawn
import monster_squirrel
import players

# 초기화
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Window")

# 색상 정의
bg_color = (230, 230, 230)  # RGB로 배경색 설정
monsters = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(players.player)
# MonsterSpawner 객체 생성
monster_spawner = spawn.MonsterSpawner(players.player, all_sprites, monsters)
monster_spawner.add_monster_class(monster_squirrel.SquirrelMonster)
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
