from classes.rewards.gem_fabric import Gem_fabric
from classes.rewards.gold_fabric import Gold_fabric
from classes.rewards.coin_fabric import Coin_fabric
from classes.rewards.food_fabric import Food_fabric
from classes.rewards.drug_fabric import Drug_fabric
from classes.rewards.poison_fabric import Poison_fabric
from classes.rewards.weapon_fabric import Weapon_fabric
from classes.game_settings import Game_settings
from classes.character_builder import Character_builder
import random


class App:
    def main(self):
        # fabric method example in game
        fab_1 = Gold_fabric()
        fab_1.open_reward()
        fab_2 = Gem_fabric()
        fab_2.open_reward()
        fab_3 = Coin_fabric()
        fab_3.open_reward()
        fab_4 = Food_fabric()
        fab_4.open_reward()
        fab_5 = Drug_fabric()
        fab_5.open_reward()
        fab_6 = Poison_fabric()
        fab_6.open_reward()
        fab_7 = Weapon_fabric()
        fab_7.open_reward()
        fabric_list = [fab_1, fab_2, fab_3, fab_4, fab_5, fab_6, fab_7]

        for i in range(20):
            index = random.randint(0, 6)
            fabric_list[index].open_reward()

        # singleton example in game
        settings1 = Game_settings(True, "Easy")
        settings1.update_settings(True, "Hard")
        settings2 = Game_settings(True, "Medium")
        settings2.update_settings(True, "Hard")
        print(settings2.difficulty_level)
        print(settings1 is settings2)

        # builder example in game
        builder = Character_builder("Warrior")
        builder.set_health(150)
        builder.set_attack_power(10)
        builder.set_defense_power(10)
        builder.set_moves(["Slash", "Shield Bash", "Heal"])
        character = builder.get_character()
        print(character)

if __name__ == '__main__':
    app_1 = App()
    app_1.main()


