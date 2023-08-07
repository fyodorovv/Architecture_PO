from abc import ABC, abstractmethod

class Item_generator(ABC):
    def open_reward(self):
        game_item = self.create_item()
        game_item.open()

    @abstractmethod
    def create_item(self):
        pass