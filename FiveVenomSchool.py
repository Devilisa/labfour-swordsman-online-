from Avatar import Avatar


class FiveVenomSchool(Avatar):

    def __init__(self, character: Avatar):
        super().__init__(character.nickname, level=10, hp=character.hp, exp=character.exp)
        self.school_damage = {'poison_damage': 20, 'earth_damage': 15, 'fire_damage': 15}
        self.earth_damage = self.school_damage['earth_damage']
        self.fire_damage = self.school_damage['fire_damage']
        self.poison_damage = self.school_damage['poison_damage']
        self.equipment['Weapon'] = 'Simple lash'

    def full_damage(self):
        return self.damage + self.earth_damage + self.poison_damage + self.fire_damage

    def use_skill(self, skill):
        tiara1 = {'Whip grip': 'whipped', 'Lash': 'lashed', 'Lash vortex': 'spinning'}
        tiara2 = {'Earth flower': 'holding', 'Poisonous flower': 'poisoning', 'Fire flower': 'burning',
                  'Healing flower': 'healing'}
        tiara3 = {'Snakes bite': 'calling snakes', 'Spiders attack': 'calling spiders',
                  'Venom beasts anger': 'all beasts attack'}
        used = False
        if skill in tiara1:
            print(tiara1[skill])
            used = True
        if self.level >= 20 and skill in tiara2:
            print(tiara2[skill])
            used = True
        elif skill in tiara2:
            print('You cannot use this skill yet')
            used = True
        if self.level >= 30 and skill in tiara3:
            print(tiara2[skill])
            used = True
        elif skill in tiara3:
            print('You cannot use this skill yet')
            used = True
        if not used:
            print('There is no such skill. Please try again')

    def put_on_equipment(self, extra_hp, extra_damage, cloth_type, cloth_name, equipment_lvl,  extra_earth_dmg,
                         extra_fire_dmg, extra_poison_dmg):
        if equipment_lvl <= self.level:
            if cloth_type in self.equipment:
                self.equipment[cloth_type] = cloth_name
            self.hp += extra_hp
            self.damage += extra_damage
            self.school_damage['earth_damage'] += extra_earth_dmg
            self.school_damage['fire_damage'] += extra_fire_dmg
            self.school_damage['poison_damage'] += extra_poison_dmg
        else:
            print('Error: not suitable level for this equipment')


def entering_school(character: Avatar):
    character = FiveVenomSchool(character)
    return character
