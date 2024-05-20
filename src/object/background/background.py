import pygame
import sys

class Background:
    def __init__(self, screen, player):
        self.width = 800
        self.height = 600
        self.screen = screen
        # 배경 이미지 불러오기
        self.background = pygame.image.load("etc/graphics/background/background.png")
        self.background_width, self.background_height = self.background.get_size()
        self.rect = self.background.get_rect()

        self.player = player

        self.health_bar_width = self.player.rect.width // 2
        self.health_bar_height = 7

    def draw(self, screen, camera_x, camera_y):
        self.screen.blit(self.background, (-camera_x, -camera_y))
        self._draw_health_bar(screen, camera_x, camera_y)

    def _draw_health_bar(self,screen, camera_x, camera_y):
        # 체력바 위치 설정
        health_bar_x = self.player.rect.x + self.player.rect.width * 0.25 - camera_x
        health_bar_y =self.player.rect.y + self.player.rect.height - 15 - camera_y

        # 현재 체력 비율 계산
        health_ratio = self.player.health / self.player.max_health
        current_health_bar_width = self.health_bar_width * health_ratio

        # 체력바 배경 그리기
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y,
                         self.health_bar_width, self.health_bar_height))
        # 현재 체력 그리기
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y,
                         current_health_bar_width, self.health_bar_height))


