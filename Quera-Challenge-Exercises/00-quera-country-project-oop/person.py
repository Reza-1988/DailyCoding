import math


class Person:

    instances = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.level = 1
        self.job = ""
        self.work_place = None
        Person.instances.append(self)

    def do_level(self, income):
        result = income * math.sqrt(self.level * self.work_place.level)
        return result

    def clac_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        return self.do_level(self.calc_income()) - self.calc_life_cost()

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1

    @staticmethod
    def calc_all():
        s = 0
        for p in Person.instances:
            s += p.calc()
        return s