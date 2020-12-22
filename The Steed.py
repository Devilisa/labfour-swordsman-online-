class TheStead:

    def __init__(self, name, speed=10, type_of_steed='horse base'):
        self.speed = speed
        self.name = name
        self.type_of_steed = type_of_steed

    def speed_up(self):
        self.speed += 5
        print('Speeding')

    def return_to_normal_speed(self):
        self.speed -= 5
        print('End of speeding')

    @staticmethod
    def jump(self):
        print('Jump')
