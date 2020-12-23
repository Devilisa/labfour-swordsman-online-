from accessify import protected
from TheSteed import TheSteed
from Familiar import Familiar


class Avatar:
    chance_to_change_nickname = 1
    exp_limit = 1000
    max_level = 99
    damage = 10

    def __init__(self, nickname, hp=1000, exp=0, level=0, steed='none', familiar='none'):
        self.nickname = nickname
        self.hp = hp
        self.exp = exp
        self.level = level
        self.steed = steed
        self.familiar = familiar
        self.equipment = {'Helmet': 'none', 'Shirt': 'none', 'Bracers': 'none', 'Pants': 'none', 'Boots': 'none',
                          'Talisman': 'none', 'Ring': 'none', 'Weapon': 'none'}

    def level_up(self):
        if self.level < self.max_level:
            self.level += 1
            self.exp = self.exp % self.exp_limit
            self.exp_limit += 1000 * self.level
            self.hp += 70 * self.level
        if self.level == 10:
            print('It is time to get your first steed!')
            name = input('Enter your steed name')
            self.get_the_steed(name)
            print('Congratulations! You have got your steed. Now it is time to get familiar!')
            name_familiar = input('Enter familiar name')
            type_familiar = input('Enter type of your familiar')
            self.get_familiar(type_familiar, name_familiar)

    def put_on_equipment(self, extra_hp, extra_damage, cloth_type, cloth_name, equipment_lvl):
        if equipment_lvl <= self.level:
            if cloth_type in self.equipment:
                self.equipment[cloth_type] = cloth_name
            self.hp += extra_hp
            self.damage += extra_damage
        else:
            print('Error: not suitable level for this equipment')

    def complete_task(self, add_exp: int):
        self.exp += add_exp
        if self.exp >= self.exp_limit:
            self.level_up()

    def change_nickname(self, new_nickname):
        if self.chance_to_change_nickname == 1:
            self.nickname = new_nickname
            self.chance_to_change_nickname = 0

    def get_personal_info(self):
        print(self.nickname)
        print(f'HP: {self.hp}')
        print(f'Level: {self.level}')
        print(f'Experience: {self.exp}')
        print(f'Damage: {self.damage}')
        print("-----------------")

    def get_equipment_info(self):
        for key, value in self.equipment.items():
            print(f'{key}: {value}')
        print('------------------')

    def full_info(self):
        self.get_personal_info()
        self.get_equipment_info()

    def attack(self, enemy):
        enemy.hp -= self.damage

    @protected
    def get_the_steed(self, name):
        steed = TheSteed(name)
        self.steed = steed

    def change_the_steed(self, name):
        name1 = TheSteed(name)
        self.steed = name1

    @protected
    def get_familiar(self, familiar_type, name):
        owner = self.nickname
        familiar = Familiar(owner, name, familiar_type)
        self.familiar = familiar
