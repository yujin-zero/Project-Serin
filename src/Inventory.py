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
        self.add_weapon(self.carrot_weapon)
        # self.add_item(self.wing_boots)
        self.add_weapon(self.apple_weapon)  # 사과 왜 돌아가지..
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

    def increase_apple_weapon_level(self):
        if self.apple_weapon.level < self.apple_weapon.maxLevel:
            self.apple_weapon.level += 1
            self.apple_weapon.add_apples()  # 사과 추가 및 위치 재설정
            for apple in self.apple_weapon.apples:
                apple.damage = self.apple_weapon.damage[self.apple_weapon.level]

    def has_carrot_weapon(self):
        return any(isinstance(weapon, CarrotWeapon) for weapon in self.weapon_list)

    def has_leaf_weapon(self):
        return any(isinstance(weapon, LeafWeapon) for weapon in self.weapon_list)

    # def increase_carrot_weapon_level(self):
    #     if self.carrot_weapon.level < self.carrot_weapon.maxLevel:
    #         self.carrot_weapon.level += 1

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
