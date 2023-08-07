from classes.Item_generator import Item_generator
from classes.rewards.weapon import Weapon

class Weapon_fabric(Item_generator):
    def create_item(self):
        return Weapon()