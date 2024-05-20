import pygame
import sys
from object.player.player import Player
from object.player.camera import Camera
from object.background.background import Background

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Serin")
        self.player = Player(self.screen_width, self.screen_height)
        self.camera = Camera(self.screen_width, self.screen_height)
        self.background = Background(self.screen, self.player)
    
    def run(self):
        self.screen.fill((0, 0, 0))

        isRunning = True
        while isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False
            self.player.move(self.background.background_width, self.background.background_height)
            self.camera.update(self.player.rect, self.background.background_width, self.background.background_height)

            self.background.draw(self.screen, self.camera.x, self.camera.y)
            self.player.draw(self.screen, self.camera.x, self.camera.y) 

            pygame.display.flip()
        
        pygame.quit()
        sys.exit()
