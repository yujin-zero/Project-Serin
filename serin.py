import pygame
import sys

# 초기화
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Window")

# 색상 정의
bg_color = (230, 230, 230)  # RGB로 배경색 설정

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 배경색 채우기
    screen.fill(bg_color)

    # 화면 업데이트
    pygame.display.flip()
