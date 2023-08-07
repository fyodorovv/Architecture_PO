from classes.Item_generator import Item_generator
from classes.rewards.gold import Gold

class Gold_fabric(Item_generator):
    def create_item(self):
        return Gold()