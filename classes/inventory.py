class item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop


# Create some Items
potion = item("Potion", 'potion', 'Heals 50 HP', 50)
hipotion = item("Hi-Potion", 'potion', 'Heals 200 HP', 200)
superpotion = item("Super Potion", 'potion', 'Heals 500 HP', 500)
elixer = item('Exlixer', "elixer", 'Fully restore HP/MP of one party member', 9999)
hielixer = item("Mega Elixer", 'elixer', "Fully restores party's HP/MP", 9999)
grenade = item("Grenade", "attack", "Deals 500 damage", 500)
