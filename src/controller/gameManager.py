import pygame
import sys
from object.player.player import Player
from object.player.camera import Camera
from object.background.background import Background
from controller.monsterManager import MonsterManager

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Serin")
        self.player = Player(self.screen_width, self.screen_height)
        self.background = Background(self.screen, self.player)
        print(self.background.background_height,self.background.background_width)
        self.camera = Camera(self.screen_width, self.screen_height,self.background.background_width,self.background.background_height)
        self.monster_manager = MonsterManager(self.player, pygame.sprite.Group(),self.screen, self.camera)
    
    def run(self):

        isRunning = True
        while isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False
            keys = pygame.key.get_pressed()

            self.player.move(self.background.background_width, self.background.background_height, keys)

            self.background.draw(self.screen, self.camera)
            self.player.draw(self.screen,self.camera.camera_rect[0],self.camera.camera_rect[1]) 

            self.camera.follow(self.player)
            self.monster_manager.spawn_monster()
            self.monster_manager.draw_monster()

            pygame.display.flip()
        
        pygame.quit()
        sys.exit()
