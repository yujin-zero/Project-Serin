from LeafWeapon import LeafWeapon
from WingBoots import WingBoots
from Heart import Heart
from AppleWeapon import AppleWeapon
from CarrotWeapon import CarrotWeapon
from HealthBoostItem import HealthBoostItem
from DamageReductionItem import DamageReductionItem


class Inventory:
    def __init__(self, Serin, Screen, weapon_sprite): 
        self.weapon_list = list()
        self.item_list = list()
        self.leaf_weapon = LeafWeapon(Serin, Screen, weapon_sprite)
        self.add_weapon(self.leaf_weapon);
        self.serin = Serin
        self.wing_boots = WingBoots()
        self.add_item(self.wing_boots);
        self.heart = Heart()


    def add_weapon(self, item):
        self.weapon_list.append(item)

    def add_item(self, item):
        self.item_list.append(item)

    def update_item(self):
        for item in self.item_list:
            item.update(self.serin)

    def attck(self):
        for item in self.weapon_list:
            item.attack()

    def heal(self):
        self.heart.update(self.serin)

   
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

    def has_health_boost_item(self):
        for item in self.item_list:
            if isinstance(item, HealthBoostItem):
                return True
        return False

    def use_health_boost_item(self, character):
        for item in self.item_list:
            if isinstance(item, HealthBoostItem):
                item.apply(character)
                # self.item_list.remove(item)
                break

    def has_damage_reduction_item(self):
        for item in self.item_list:
            if isinstance(item, DamageReductionItem):
                return True
        return False

