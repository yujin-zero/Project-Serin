from LeafWeapon import LeafWeapon
from WingBoots import WingBoots
from Heart import Heart
from AppleWeapon import AppleWeapon
from CarrotWeapon import CarrotWeapon
from HealthBoostItem import HealthBoostItem
from DamageReductionItem import DamageReductionItem
from WhipWeapon import WhipWeapon


class Inventory:
    def __init__(self, Serin, Screen, weapon_sprite):
        self.serin = Serin

        self.weapon_list = list()
        self.item_list = list()
        self.leaf_weapon = LeafWeapon(Serin, Screen, weapon_sprite)
        self.apple_weapon = AppleWeapon(Serin, Screen, weapon_sprite)
        self.wing_boots = WingBoots()
        self.heart = Heart()
        self.carrot_weapon = CarrotWeapon(Serin, Screen, weapon_sprite)
        self.whip_weapon = WhipWeapon(Serin, Screen, weapon_sprite)
        
        # self.add_weapon(self.leaf_weapon)
        # self.add_weapon(self.carrot_weapon)
        # self.add_item(self.wing_boots)
        self.add_weapon(self.apple_weapon)
        # self.add_weapon(self.whip_weapon)

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
