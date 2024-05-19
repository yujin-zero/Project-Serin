import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 1300
        self.screen_height = 800
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("밤의 어쩌구 세린")
        self.bg_color = (230, 230, 230)
        self.clock = pygame.time.Clock()
        self.running = True
        self.serin = Serin(self.screen_width // 2, self.screen_height // 2)

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        self.serin.update()

    def _draw(self):
        self.screen.fill(self.bg_color)
        self.serin.draw(self.screen)
        pygame.display.flip()


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

    def draw(self, screen):
        screen.blit(self.frames[self.frame_index], self.rect)
        self._draw_health_bar(screen)

    def _draw_health_bar(self, screen):
        # 체력바 위치 설정
        health_bar_x = self.rect.x + self.rect.width * 0.25
        health_bar_y = self.rect.y + self.rect.height - 15

        # 현재 체력 비율 계산
        health_ratio = self.health / self.max_health
        current_health_bar_width = self.health_bar_width * health_ratio

        # 체력바 배경 그리기
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y,
                         self.health_bar_width, self.health_bar_height))
        # 현재 체력 그리기
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y,
                         current_health_bar_width, self.health_bar_height))


if __name__ == "__main__":
    game = Game()
    game.run()
