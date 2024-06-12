import pygame
import math


class WhipWeapon:
    def __init__(self, serin, screen, all_sprites):
        self.serin = serin
        self.screen = screen
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = [0, 1000, 900, 900, 800, 700]
        self.damage = [0, 20, 20, 25, 30, 30]
        self.level = 1
        self.image = pygame.image.load(
            "./image/whipAttack.png").convert_alpha()
        self.max_level = 5
        self.all_sprites = all_sprites
        self.images = [
            pygame.image.load(f"./image/whip/whipAttack1.png").convert_alpha(),
            pygame.image.load(f"./image/whip/whipAttack2.png").convert_alpha(),
            pygame.image.load(f"./image/whip/whipAttack3.png").convert_alpha(),
        ]
        
        self.sound = pygame.mixer.Sound("sound/sword_swing.wav")

    def attack(self):
        if self.level == 0:
            return
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay[self.level]:
            self.last_shot = now
            base_angle = math.radians(0)

            if self.serin.direction < 0:
                # 캐릭터가 왼쪽을 바라볼 때 이미지를 좌우로 반전시킵니다.
                images = [pygame.transform.flip(
                    image, True, False) for image in self.images]
                whip = Whip(self.serin.rect.centerx - 100, self.serin.rect.centery -
                            30, base_angle, self.damage[self.level], images)

            else:
                images = self.images
                whip = Whip(self.serin.rect.centerx + 100, self.serin.rect.centery -
                            30, base_angle, self.damage[self.level], images)

            self.all_sprites.add(whip)
            self.sound.play()


class Whip(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, damage, images):
        super().__init__()
        self.images = [pygame.transform.scale(
            image, (image.get_width() // 2, image.get_height() // 2)) for image in images]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = angle
        self.damage = damage
        self.creation_time = pygame.time.get_ticks()
        self.animation_speed = 100

    def update(self):
        self.image = pygame.transform.rotate(
            self.images[self.image_index], -math.degrees(self.angle))
        self.rect = self.image.get_rect(center=self.rect.center)

        now = pygame.time.get_ticks()
        if now - self.creation_time > self.animation_speed:
            self.creation_time = now
            self.image_index += 1
            if self.image_index >= len(self.images):
                self.kill()

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (self.rect.x -
                    camera_x, self.rect.y - camera_y))
