from .work_place import WorkPlace, Consts


class Company(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "company"

    def calc_capacity(self):
        self.capacity = self.level

    def calc_costs(self):
        costs = Consts.BASE_PLACE_COST * self.level
        return int(costs)