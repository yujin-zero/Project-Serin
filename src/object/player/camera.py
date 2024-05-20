import pygame 
class Camera:
    def __init__(self, screen_width, screen_height, world_width, world_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.world_width = world_width
        self.world_height = world_height
        self.camera_rect = pygame.Rect(0, 0, screen_width, screen_height)
    
    def follow(self, target):
        self.camera_rect.center = target.rect.center
        print(self.camera_rect[0])

        self.camera_rect.clamp_ip(pygame.Rect(0, 0, self.world_width, self.world_height))
