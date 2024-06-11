import pygame


class WingBoots:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./image/wingBoots.png").convert_alpha()
        self.level = 1

    def get_boost_amount(self):
        boost_amounts = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
        return boost_amounts.get(self.level, 1)

    def update(self, Serin):
        boost_amount = self.get_boost_amount()
        base = Serin.base_speed
        base += boost_amount
        # print(Serin.base_speed)
        Serin.speed = base
