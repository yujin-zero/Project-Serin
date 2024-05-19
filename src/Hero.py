import pygame

class Hero:
    def __init__(self, image_path, start_x, start_y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.to_x = 0
        self.to_y = 0
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.to_x -= 3
            elif event.key == pygame.K_RIGHT:
                self.to_x += 3
            elif event.key == pygame.K_UP:
                self.to_y -= 3
            elif event.key == pygame.K_DOWN:
                self.to_y += 3
        
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.to_x = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                self.to_y = 0
    
    def move(self, boundary_width, boundary_height):
        self.rect.x += self.to_x
        self.rect.y += self.to_y

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > boundary_width - self.rect.width:
            self.rect.x = boundary_width - self.rect.width
        
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > boundary_height - self.rect.height:
            self.rect.y = boundary_height - self.rect.height
    
    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))
