import pygame

class Background:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.width, self.height = self.image.get_size()
    
    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (-camera_x, -camera_y))
        
    def get_surface(self):
        return self.image
