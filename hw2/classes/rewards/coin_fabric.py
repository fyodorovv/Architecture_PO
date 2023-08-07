from classes.Item_generator import Item_generator
from classes.rewards.coin import Coin

class Coin_fabric(Item_generator):
    def create_item(self):
        return Coin()