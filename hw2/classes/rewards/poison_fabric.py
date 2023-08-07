from classes.Item_generator import Item_generator
from classes.rewards.poison import Poison

class Poison_fabric(Item_generator):
    def create_item(self):
        return Poison()