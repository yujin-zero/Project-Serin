import monster
import Serin

class SpiritMonster(monster.Monster):
    def __init__(self, x, y, player):
        image_paths = [
            f"./10 - Enemies/graphics/monsters/spirit/move/{i}.png" for i in range(4)]
        super().__init__(x, y, health=150, speed=0.7, power=0.2,
                         image_paths=image_paths, player=player, size=(50, 50))
