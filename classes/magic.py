import random

class spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)


# Create While Magic
fire = spell('Fire', 9, 110, 'black')
thunder = spell('Thunder', 10, 150, 'black')
blizzard = spell('Blizzard', 15, 200, 'black')
meteor = spell('Meteor', 20, 200, 'black')
quake = spell('Quake', 6, 50, 'black')

# Create White Magic
cure = spell("Cure", 10, 150, 'white')
cura = spell("Cura", 20, 250, 'white')
