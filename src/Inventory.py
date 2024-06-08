from LeafWeapon import LeafWeapon;


class Inventory:
    def __init__(self, Serin, Screen, weapon_sprite): 
        self.item_list = list()
        self.leaf_weapon = LeafWeapon(Serin, Screen, weapon_sprite)
        self.add_item(self.leaf_weapon);

    def add_item(self, item):
        self.item_list.append(item)

    def attck(self):
        for item in self.item_list:
            print(item)
            item.attack()
    

