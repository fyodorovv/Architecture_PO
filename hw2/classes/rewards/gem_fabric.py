from classes.Item_generator import Item_generator
from classes.rewards.gem import Gem

class Gem_fabric(Item_generator):
    def create_item(self):
        return Gem()