import pygame
import sys
from object.enemy.monster import Monster
class SquirrelMonster(Monster):
    def __init__(self, x, y, player):
        print("spawned!")
        image_path = [f"etc/graphics/monster/raccoon/move/{i}.png" for i in range(5)]
        super().__init__(x, y,player=player, health=80, speed=1, power=5, image_path=image_path ,size=(50, 50))
