import pygame


class Serin:
    def __init__(self, x, y):
        self.original_frames = [pygame.image.load(
            f'./moving/{i}.png') for i in range(1, 13)]

        # 이미지 크기 1.5배로 조정
        self.frames = [pygame.transform.scale(frame, (int(frame.get_width(
        ) * 1.7), int(frame.get_height() * 1.7))) for frame in self.original_frames]

        self.rect = self.frames[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.frame_index = 0
        self.frame_count = 6
        self.frame_delay = 100
        self.last_update_time = pygame.time.get_ticks()

        self.health = 50
        self.max_health = 50
        self.health_bar_width = self.rect.width // 2
        self.health_bar_height = 7

    def update(self, boundary_width, boundary_height):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if current_time - self.last_update_time > self.frame_delay:
                self.frame_index = (self.frame_index + 1) % self.frame_count
                self.last_update_time = current_time
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if current_time - self.last_update_time > self.frame_delay:
                self.frame_index = 6 + \
                    (self.frame_index + 1) % self.frame_count
                self.last_update_time = current_time
        else:
            if self.frame_index < 6:
                self.frame_index = 0
            else:
                self.frame_index = 6

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # 경계 설정
        self.rect.x = max(
            0, min(self.rect.x, boundary_width - self.rect.width))
        self.rect.y = max(
            0, min(self.rect.y, boundary_height - self.rect.height))

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.frames[self.frame_index],
                    (self.rect.x - camera_x, self.rect.y - camera_y))
        self._draw_health_bar(screen, camera_x, camera_y)

    def _draw_health_bar(self, screen, camera_x, camera_y):
        # 체력바 위치 설정
        health_bar_x = self.rect.x - camera_x + self.rect.width * 0.25
        health_bar_y = self.rect.y - camera_y + self.rect.height - 15

        # 현재 체력 비율 계산
        health_ratio = self.health / self.max_health
        current_health_bar_width = self.health_bar_width * health_ratio

        # 체력바 배경 그리기
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y,
                         self.health_bar_width, self.health_bar_height))
        # 현재 체력 그리기
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y,
                         current_health_bar_width, self.health_bar_height))
