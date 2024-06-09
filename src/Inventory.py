from LeafWeapon import LeafWeapon
from WingBoots import WingBoots
from Heart import Heart

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

    

