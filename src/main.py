import pygame
import sys
from Background import Background
from Camera import Camera
from Serin import Serin


class Main:
    def __init__(self):
        pygame.init()
        self.screen_width = 1300
        self.screen_height = 800
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("밤의 어쩌구 세린")

        self.background = Background("./image/background.png")
        self.serin = Serin(self.screen_width // 2, self.screen_height // 2)
        self.clock = pygame.time.Clock()
        self.camera = Camera(self.screen_width, self.screen_height)
        self.running = True

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
        # self.serin.update()
        self.serin.update(self.background.width, self.background.height)
        self.camera.update(
            self.serin.rect, self.background.width, self.background.height)

    def _draw(self):
        self.background.draw(self.screen, self.camera.x, self.camera.y)
        # self.serin.draw(self.screen)
        self.serin.draw(self.screen, self.camera.x, self.camera.y)
        pygame.display.flip()


if __name__ == "__main__":
    Main().run()
