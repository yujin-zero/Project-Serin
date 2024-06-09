import pygame

class Serin(pygame.sprite.Sprite):
    def __init__(self, x, y, boundary_width, boundary_height):
        super().__init__()
        self.original_frames = [pygame.image.load(f'./moving/{i}.png') for i in range(1, 13)]

        # 이미지 크기 1.5배로 조정
        self.frames = [pygame.transform.scale(frame, (int(frame.get_width() * 1.7), int(frame.get_height() * 1.7))) for frame in self.original_frames]

        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # 초기 위치를 중심으로 설정
        self.base_speed = 2
        self.speed = 2
        self.frame_index = 0
        self.frame_count = 6
        self.frame_delay = 100
        self.last_update_time = pygame.time.get_ticks()

        self.health = 50
        self.max_health = 50
        self.health_bar_width = self.rect.width // 2
        self.health_bar_height = 7

        self.boundary_width = boundary_width
        self.boundary_height = boundary_height

        # Hitbox 설정 (원래 rect보다 작은 크기)
        self.hitbox = self.rect.inflate(-75, -45)  # 너비와 높이를 각각 100픽셀 줄임

    def update(self):
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
                self.frame_index = 6 + (self.frame_index + 1) % self.frame_count
                self.last_update_time = current_time
        else:
            self.frame_index = 0 if self.frame_index < 6 else 6

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # 경계 설정
        self.rect.x = max(0, min(self.rect.x, self.boundary_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, self.boundary_height - self.rect.height))

        self.image = self.frames[self.frame_index]
        # Hitbox 업데이트
        self.hitbox.center = self.rect.center

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))
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

# ... 나머지 게임 루프 및 기타 코드
