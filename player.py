class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.focus = 5
        self.resolve = 5
        self.luck = 1.0
        self.inventory = []

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} loses {amount} vitality. Remaining: {self.hp}")

    def is_alive(self):
        return self.hp > 0
