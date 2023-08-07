from classes.character import Character


class Character_builder:
    '''
    Character creates and customizes its characteristics
    '''
    def __init__(self, name):
        self.character = Character(name)

    def set_health(self, health):
        self.character.health = health

    def set_attack_power(self, attack_power):
        self.character.attack_power = attack_power

    def set_defense_power(self, defense_power):
        self.character.defense_power = defense_power

    def set_moves(self, moves):
        self.character.moves = moves

    def get_character(self):
        return self.character