import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        if self.hp == 0:
            print(f'{self.name} has died in battle')

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(f'\n{bcolors.BOLD}{self.name}{bcolors.ENDC}')
        print(f'{bcolors.OKBLUE}{bcolors.BOLD}   Action:{bcolors.ENDC}')
        for item in self.actions:
            print("\t"+str(i) + ". " + item)
            i += 1

    def choose_magic(self):
        i = 1
        print(f"\n{bcolors.OKBLUE}{bcolors.BOLD}   Magic:{bcolors.ENDC}")
        for spell in self.magic:
            print("\t", str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print(f'\n{bcolors.OKGREEN}{bcolors.BOLD}   Item:{bcolors.ENDC}')
        available_items = [item for item in self.items if item['quantity'] > 0]

        for item in available_items:
            print(f"\t{str(i)}. {item['item'].name}: {str(item['item'].description)} x {str(item['quantity'])}")
            i += 1

    def get_stats(self):
        hp_ticks = int(self.hp / self.maxhp * 20)
        hp_bar = "█"*hp_ticks + " "*(20 - hp_ticks)

        mp_ticks = int(self.mp / self.maxmp * 10)
        mp_bar = "█" * mp_ticks + " " * (10 - mp_ticks)

        pad = ' ' * (10 - len(str(self.name))) + ' ' * (8-len(str(self.hp))-len(str(self.maxhp)))

        print(f"{bcolors.BOLD}{self.name}:{pad}{self.hp}/{self.maxhp} "
              f"|{bcolors.OKGREEN}{hp_bar}{bcolors.ENDC}{bcolors.BOLD}| ", end="")
        print(f"{' '*(6-len(str(self.mp))-len(str(self.maxmp)))}{self.mp}/{self.maxmp} "
              f"|{bcolors.OKBLUE}{mp_bar}{bcolors.ENDC}|")

    def choose_target(self, enemies):
        i = 1
        print(f'\n{bcolors.FAIL}{bcolors.BOLD}   Target:{bcolors.ENDC}')
        for enemy in enemies:
            print(f"\t{str(i)}.{enemy.name}")
            i += 1
        return enemies[int(input("Choice: ")) - 1]

    def get_enemy_stats(self):
        hp_ticks = int(self.hp / self.maxhp * 40)
        hp_bar = hp_ticks * "█"
        no_hp_bar = int(40 - hp_ticks) * "█"

        pad = ' ' * (18 - len(str(self.name)) - len(str(self.hp)) - len(str(self.maxhp)))

        print(f"{bcolors.BOLD}{self.name}:{pad}{self.hp}/{self.maxhp} "
              f"|{bcolors.FAIL}{hp_bar}{bcolors.ENDC}{no_hp_bar}{bcolors.BOLD}| ")

    def get_move(self, players, enemies):
        run = True
        while run:
            if self.hp == 0:
                break

            self.choose_action()
            choice = input('Choice: ')
            index = int(choice) - 1

            if index == 0:
                dmg = self.generate_damage()
                target = self.choose_target(enemies)
                target.take_damage(dmg)
                print(f"{self.name} attacks {target.name} for {str(dmg)} damage ({target.hp}/{target.maxhp})")
                break

            elif index == 1:
                self.choose_magic()
                magic_choice = int(input('Choice: ')) - 1

                if magic_choice == -1:
                    continue

                spell = self.magic[magic_choice]
                magic_dmg = spell.generate_damage()

                current_mp = self.get_mp()
                if spell.cost > current_mp:
                    print(f'{bcolors.FAIL} \nNot enough MP\n {bcolors.ENDC}')
                    continue

                self.reduce_mp(spell.cost)

                if spell.type == 'white':
                    self.heal(magic_dmg)
                    print(f'{bcolors.OKBLUE}{spell.name} heals for {magic_dmg} HP.{bcolors.ENDC}')
                    break

                elif spell.type == 'black':
                    target = self.choose_target(enemies)
                    target.take_damage(magic_dmg)
                    print(f'{bcolors.OKBLUE} \n{spell.name} deals {magic_dmg} points of damage to '
                          f'{target.name}({target.hp}/{target.maxhp}){bcolors.ENDC}')
                    break

            elif index == 2:
                self.choose_item()
                item_choice = int(input('Choice: ')) - 1

                if item_choice == -1 or self.items[item_choice]['quantity'] <= 0:
                    continue

                item = self.items[item_choice]['item']
                self.items[item_choice]['quantity'] -= 1

                if item.type == "potion":
                    self.heal(item.prop)
                    print(f'{bcolors.OKGREEN}\n{item.name} heals for {str(item.prop)} HP {bcolors.ENDC}')
                    break

                elif item.type == 'elixer':
                    if item.name == "MegaElixer":
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                            break
                    self.hp = self.maxhp
                    self.mp = self.maxmp
                    print(f'{bcolors.OKGREEN}\n{item.name} fully restores HP/MP {bcolors.ENDC}n')
                    break

                elif item.type == 'attack':
                    target = self.choose_target(enemies)
                    target.take_damage(item.prop)
                    print(f'{bcolors.FAIL}\n{item.name} deals {str(item.prop)} points of damage to '
                          f'{target.name}({target.hp}/{target.maxhp}){bcolors.ENDC}')
                    break
