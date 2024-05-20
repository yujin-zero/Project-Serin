import pygame
import sys
from controller.gameManager import GameManager
class Main:
    def __init__(self):
        self.game_manager = GameManager()

    def run(self):
        self.game_manager.run()

if __name__ == "__main__":
    main = Main()
    main.run()