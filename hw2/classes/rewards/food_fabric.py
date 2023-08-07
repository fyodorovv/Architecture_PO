from classes.Item_generator import Item_generator
from classes.rewards.food import Food

class Food_fabric(Item_generator):
    def create_item(self):
        return Food()