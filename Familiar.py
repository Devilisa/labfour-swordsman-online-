class Familiar:
    familiar_type = {'school': 'Uses school skill', 'animal': 'Attack enemy', 'bird': 'Strike of wings'}

    def __init__(self, owner, name, type_of_familiar):
        self.owner = owner
        self.name = name
        try:
            self.special_skill = self.familiar_type[type_of_familiar]
        except:
            print('You entered wrong type and that is why you do not get special skill')
            self.special_skill = 'no such skill'
        self.skills = {1: 'Opens character post', 2: 'Opens character warehouse', 3: 'Collects things',
                       4: 'Opens friends list', 5: self.special_skill}

    def use_skills(self, skill):
        if skill in self.skills:
            print(self.skills[skill])
        else:
            print('Familiar does not have such skill')
