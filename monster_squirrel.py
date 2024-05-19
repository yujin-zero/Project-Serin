import pygame
import sys
import random
import math
import monster
import players
class SquirrelMonster(monster.Monster):
    def __init__(self, x, y):
        image_paths = [f"./10 - Enemies/graphics/monsters/raccoon/move/{i}.png" for i in range(5)]
        super().__init__(x, y, health=80, speed=0.2, power=5, image_paths=image_paths,player=players.player, size=(50, 50))
