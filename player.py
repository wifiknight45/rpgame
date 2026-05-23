class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.focus = 6
        self.resolve = 6
        self.luck = 1.0
        self.inventory = []

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} loses {amount} vitality. Remaining vitality {self.hp}")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} regains {amount} vitality. Current vitality {self.hp}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} obtains {item}")

    def is_alive(self):
        return self.hp > 0
