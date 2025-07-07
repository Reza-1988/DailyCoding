class Drug:

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

class Pharmacy:

    def __init__(self, name):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug):
        self.drugs.append(drug)

    def add_employee(self, first_name, last_name, age):
        employee_dict = {'first_name': first_name, 'last_name': last_name, 'age': age}
        self.employees.append(employee_dict)

    def total_value(self):
        total_value = 0
        for drug in self.drugs:
            drug_value = drug.price * drug.amount
            total_value += drug_value
        return total_value

    def employees_summary(self):
        i = 1
        summary = "Employees:\n"
        for employee in self.employees:
            summary += f"The employee number {i} is {employee['first_name']} {employee['last_name']} who is {employee['age']} years old.\n"
            i += 1
        return summary
