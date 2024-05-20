import pygame
import sys
import monster
import player
import player.player

class SquirrelMonster(monster.Monster):
    def __init__(self, x, y):
        print("spawned!")
        image_paths = [f"etc/graphics/monster/raccoon/move/{i}.png" for i in range(5)]
        super().__init__(x, y, health=80, speed=0.2, power=5, image_paths=image_paths,player=player.player, size=(50, 50))
