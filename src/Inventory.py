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

        # 무기 아이템
        self.weapon_list = list()
        self.leaf_weapon = LeafWeapon(Serin, Screen, weapon_sprite)
        self.apple_weapon = AppleWeapon(Serin, Screen, weapon_sprite)
        self.carrot_weapon = CarrotWeapon(Serin, Screen, weapon_sprite)
        self.whip_weapon = WhipWeapon(Serin, Screen, weapon_sprite)

        # 능력치 아이템
        self.item_list = list()
        self.item2_list = list()
        self.wing_boots = WingBoots()
        self.heart = Heart()
        self.damage_reduction = DamageReductionItem()
        self.health_boost = HealthBoostItem()

        # self.add_item(self.wing_boots)
        # self.add_item2(self.heart)
        # self.add_item2(self.health_boost)
        # self.add_item2(self.damage_reduction)

        # self.add_weapon(self.leaf_weapon)
        # self.add_weapon(self.carrot_weapon)
        self.add_weapon(self.apple_weapon)
        # self.add_weapon(self.whip_weapon)

    def add_weapon(self, item):
        self.weapon_list.append(item)

    def add_item(self, item):
        self.item_list.append(item)

    def add_item2(self, item):
        self.item2_list.append(item)

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

    def has_whip_weapon(self):
        return any(isinstance(weapon, WhipWeapon) for weapon in self.weapon_list)

    def has_wing_boots(self):
        return any(isinstance(item, WingBoots) for item in self.item_list)

    def has_heart(self):
        return any(isinstance(item, Heart) for item in self.item2_list)

    def has_damage_reduction(self):
        return any(isinstance(item, DamageReductionItem) for item in self.item2_list)

    def has_health_boost(self):
        return any(isinstance(item, HealthBoostItem) for item in self.item2_list)
