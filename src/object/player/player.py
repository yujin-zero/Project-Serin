import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        self.original_frames = [pygame.image.load(
            f'etc/graphics/player/idle/{i}.png') for i in range(1, 13)]
        
        # 이미지 크기 1.5배로 조정
        self.frames = [pygame.transform.scale(frame, (int(frame.get_width(
        ) * 1.7), int(frame.get_height() * 1.7))) for frame in self.original_frames]

        self.rect = self.frames[0].get_rect()
        self.rect.x = screen_width/2
        self.rect.y = screen_height/2
        self.speed = 20
        self.frame_index = 0
        self.frame_count = 6
        self.frame_delay = 60
        self.last_update_time = pygame.time.get_ticks()

        self.screen_width = screen_width;
        self.screen_height = screen_height;

        self.health = 50
        self.max_health = 50

    def update(self):
        self.move()
    
    #def update_health(self):

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.frames[self.frame_index], (self.rect.x - camera_x, self.rect.y - camera_y))

    def move(self, background_width, background_height, keys):
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

        # 배경 경계 체크
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > background_width - self.rect.width:
            self.rect.x = background_width - self.rect.width
        
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y  > background_height - self.rect.height:
            self.rect.y = background_height - self.rect.height
