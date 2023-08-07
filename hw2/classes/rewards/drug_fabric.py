from classes.Item_generator import Item_generator
from classes.rewards.drug import Drug

class Drug_fabric(Item_generator):
    def create_item(self):
        return Drug()