from AppleWeapon import AppleWeapon
from CarrotWeapon import CarrotWeapon


class Inventory:
    def __init__(self):
        self.item_list = []

    def add_item(self, item):
        self.item_list.append(item)

    def has_apple_weapon(self):
        for item in self.item_list:
            if isinstance(item, AppleWeapon):
                return True
        return False

    def has_carrot_weapon(self):
        for item in self.item_list:
            if isinstance(item, CarrotWeapon):
                return True
        return False
