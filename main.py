from classes.game import Person, bcolors
from classes.magic import *
from classes.inventory import *
import random

player_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{'item': potion, 'quantity': 5}, {'item': hipotion, 'quantity': 2},
                {'item': superpotion, 'quantity': 1}, {'item': elixer, 'quantity': 1},
                {'item': hielixer, 'quantity': 1}, {'item': grenade, 'quantity': 1}]

# Instantiate People
player1 = Person("Knight", 460, 65, 60, 60, player_magic, player_items)
player2 = Person("Barbarian", 330, 30, 100, 50, [], [])
player3 = Person("Mage", 90, 120, 30, 15, player_magic, [])

enemy1 = Person("Sephiroth", 5000, 300, 150, 25, [fire], [])
enemy2 = Person("Henchman", 1200, 0, 50, 10, [], [])
enemy3 = Person("Hench Woman", 900, 0, 60, 10, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
# Print Health
    for enemy in enemies:
        enemy.get_enemy_stats()
    print('')
    print("Name              HP                               MP")
    for player in players:
        player.get_stats()

# Players Move
    live_players = [player for player in players if player.hp > 0]
    for player in players:
        live_enemies = [player for player in enemies if player.hp > 0]
        player.get_move(players, live_enemies)

# Enemies Move
    print('')
    live_enemies = [player for player in enemies if player.hp > 0]
    for enemy in live_enemies:
        target = random.choice(live_players)
        enemy_dmg = enemy.generate_damage()
        target.take_damage(enemy_dmg)
        print(f"{enemy.name} attacks {target.name} for {enemy_dmg} points of damage")
    print('')

# Game Finish Conditions
    if all(enemy.get_hp() == 0 for enemy in enemies):
        print(f'{bcolors.OKGREEN} You win! {bcolors.ENDC}')
        running = False
    elif all([player.get_hp() == 0 for player in players]):
        print(f'{bcolors.FAIL} Your enemy has defeated you!' + bcolors.ENDC)
        running = False
