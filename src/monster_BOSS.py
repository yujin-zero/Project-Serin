import monster
import Serin

class BossMonster(monster.Monster):
    def __init__(self, x, y, player):
        image_paths = [
            f"./10 - Enemies/graphics/monsters/boss.png"]
        super().__init__(x, y, health=999999, speed=5, power=3,
                         image_paths=image_paths, player=player, size=(100, 200))
