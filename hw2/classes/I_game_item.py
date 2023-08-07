from abc import ABC, abstractmethod

class I_game_item(ABC):
    @abstractmethod
    def open(self):
        pass