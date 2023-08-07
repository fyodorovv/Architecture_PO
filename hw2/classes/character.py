class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
        self.defense_power = 5
        self.moves = []

    def __str__(self):
        return f"Character: {self.name}\nHealth: {self.health}\nAttack Power: {self.attack_power}\nDefense Power: {self.defense_power}\nMoves: {', '.join(self.moves)}"