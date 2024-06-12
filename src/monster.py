import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, health, speed, power, image_paths, player, size=(30, 30)):
        super().__init__()
        self.player = player
        self.images = [pygame.transform.scale(pygame.image.load(
            img).convert_alpha(), size) for img in image_paths]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # 초기 위치를 중심으로 설정
        self.health = health
        self.speed = speed
        self.power = power
        self.float_x = float(self.rect.x)
        self.float_y = float(self.rect.y)
        self.animation_index = 0
        self.animation_time = pygame.time.get_ticks()
        self.animation_delay = 100  # 밀리초 단위로 애니메이션 지연 시간 설정
        self.hitbox = self.rect.inflate(-10, -10)
        self.invulnerable = False
        self.invulnerable_time = 250
        self.last_hit_time = 0  # 마지막 피격 시간
        self.sound = pygame.mixer.Sound("sound/hit.wav")
        self.sound.set_volume(0.1)

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_time > self.animation_delay:
            self.animation_time = current_time
            self.animation_index = (
                self.animation_index + 1) % len(self.images)
            self.image = self.images[self.animation_index]
        
        #무적시간이 지나면 무적 비활성화
        if current_time - self.last_hit_time > self.invulnerable_time:
            self.invulnerable = False  


        # 플레이어의 중심을 향해 이동
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery
        dist = (dx**2 + dy**2)**0.5
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
        self.float_x += dx * self.speed
        self.float_y += dy * self.speed
        self.rect.centerx = int(self.float_x)
        self.rect.centery = int(self.float_y)
        self.hitbox.center = self.rect.center
        if self.health <= 0:
            self.kill()
    
    def hit(self, damage):
        if not self.invulnerable:  # 몬스터가 무적 상태가 아닌 경우에만 피격 효과 적용
            # 피격 효과 및 무적 상태 활성화
            self.health -= damage
            self.invulnerable = True
            self.last_hit_time = pygame.time.get_ticks()
            self.sound.play()


    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))
