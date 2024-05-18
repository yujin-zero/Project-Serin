import pygame
import sys

# 초기화
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Window")

# 배경 이미지 불러오기
background = pygame.image.load("./image\\background.png")
background_width, background_height = background.get_size()

# 캐릭터(스프라이트) 불러오기
hero = pygame.image.load("./image\\hero.png")
hero_rect = hero.get_rect()
hero_width = hero_rect.width
hero_height = hero_rect.height

# hero를 배경 이미지의 중앙에 위치시키기
hero_rect.center = (background_width // 2, background_height // 2)

# 이동할 좌표
to_x = 0
to_y = 0

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 3
            elif event.key == pygame.K_RIGHT:
                to_x += 3
            elif event.key == pygame.K_UP:
                to_y -= 3
            elif event.key == pygame.K_DOWN:
                to_y +=3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # hero 이동
    hero_rect.x += to_x
    hero_rect.y += to_y

    # 배경 경계 체크
    if hero_rect.x < 0:
        hero_rect.x = 0
    elif hero_rect.x > background_width - hero_width:
        hero_rect.x = background_width - hero_width
    
    if hero_rect.y < 0:
        hero_rect.y = 0
    elif hero_rect.y > background_height - hero_height:
        hero_rect.y = background_height - hero_height

    # 카메라 좌표 설정
    camera_x = hero_rect.x - screen_width // 2 + hero_width // 2
    camera_y = hero_rect.y - screen_height // 2 + hero_height // 2

    # 카메라 경계 체크
    camera_x = max(0, min(camera_x, background_width - screen_width))
    camera_y = max(0, min(camera_y, background_height - screen_height))

    # 배경화면 그리기
    screen.blit(background, (-camera_x, -camera_y))

    # hero 그리기
    screen.blit(hero, (hero_rect.x - camera_x, hero_rect.y - camera_y))

    # 화면 업데이트
    pygame.display.flip()
