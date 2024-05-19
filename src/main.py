import pygame
import sys
from Background import Background
from Hero import Hero
from Camera import Camera

class Main:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pygame Window")

        self.background = Background("./image/background.png")
        self.hero = Hero("./image/hero.png", self.background.width // 2, self.background.height // 2)
        self.camera = Camera(self.screen_width, self.screen_height)
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                self.hero.handle_event(event)
            
            self.hero.move(self.background.width, self.background.height)
            self.camera.update(self.hero.rect, self.background.width, self.background.height)

            self.screen.fill((0, 0, 0))
            self.background.draw(self.screen, self.camera.x, self.camera.y)
            self.hero.draw(self.screen, self.camera.x, self.camera.y)

            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Main().run()
