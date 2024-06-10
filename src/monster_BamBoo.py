import monster
import Serin

class BamBooMonster(monster.Monster):
    def __init__(self, x, y, player):
        image_paths = [
            f"./10 - Enemies/graphics/monsters/bamboo/move/{i}.png" for i in range(4)]
        super().__init__(x, y, health=300, speed=0.3, power=0.1,
                         image_paths=image_paths, player=player, size=(50, 50))
