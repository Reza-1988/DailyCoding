class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"


class Consts:
    # You can change these numbers to your custom prices
    BASE_PRICE = {'mine': 300, 'school': 100, 'company': 200}
    BASE_PLACE_COST = 1000
    LEVEL_MUL = 10


class WorkPlace:

    instances = []

    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = []
        self.capacity = 1
        WorkPlace.instances.append(self)

    def get_price(self) -> int:
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self):
        self.level += 1
        self.calc_capacity()

    def hire(self, person):
        if len(self.employees) >= self.capacity:
            raise WorkPlaceIsFull()
        else:
            self.employees.append(person)
            person.work_place = self

    def get_expertise(self) -> str:
        return self.expertise

    def calc(self) -> int:
        return - self.calc_costs()

    @staticmethod
    def calc_all() -> int:
        s = 0
        for w in WorkPlace.instances:
            s -= w.calc()
        return s



