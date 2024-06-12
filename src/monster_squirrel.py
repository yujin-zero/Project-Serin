import monster
import Serin


class SquirrelMonster(monster.Monster):
    def __init__(self, x, y, player):
        image_paths = [
            f"./10 - Enemies/graphics/monsters/raccoon/move/{i}.png" for i in range(5)]
        super().__init__(x, y, health=80, speed=1, power=0.2,
                         image_paths=image_paths, player=player, size=(50, 50))
