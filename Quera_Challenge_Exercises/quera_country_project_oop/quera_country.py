# Importing Person classes
from manage_employees.person import Person
from manage_employees.engineer import Engineer
from manage_employees.teacher import Teacher
from manage_employees.worker import Worker

# Importing WorkPlace classes
from manage_work_place.work_place import WorkPlace, WorkPlaceIsFull, Consts as WorkPlaceConsts
from manage_work_place.mine import Mine
from manage_work_place.school import School
from manage_work_place.company import Company

# STEP 1: Creating People

# Creating an engineer
raha = Engineer(name="Raha", age=30)

# Creating a teacher
sara = Teacher(name="Sara", age=25)

# Creating a worker
taha = Worker(name="Taha", age=22)

print(f"Total number of people: {len(Person.instances)}")
for p in Person.instances:
    print(f"- {p.name} ({p.get_job()}), Level: {p.level}")

# STEP 2: Creating Workplaces
# Creating a mine
kavir_mine = Mine(name="Kavir Mine")

# Creating a school
danesh_school = School(name="Danesh School")

# Creating a company
pishro_company = Company(name="Pishro Company")

print(f"\nTotal number of workplaces: {len(WorkPlace.instances)}")
for wp in WorkPlace.instances:
    print(f"- {wp.name} ({wp.get_expertise()}), Level: {wp.level}, Initial Capacity: {wp.capacity}")

# STEP 3: Hiring people in workspace

try:
    kavir_mine.hire(taha)
    print(f"\n{taha.name} was hired at {taha.work_place.name}.")

    danesh_school.hire(sara)
    print(f"{sara.name} was hired at {sara.work_place.name}.")

    pishro_company.hire(raha)
    print(f"{raha.name} was hired at {raha.work_place.name}.")

    print(f"Employees of {pishro_company.name}: {[e.name for e in pishro_company.employees]}")

    # Attempting to hire beyond capacity
    kamran = Engineer(name="Kamran", age=35)
    pishro_company.hire(kamran) # This line would raise an error

except WorkPlaceIsFull as e:
    print(f"Hiring error: {e}")


# STEP 4: Upgrade level

print(f"\nInitial level of {raha.name}: {raha.level}")
raha.upgrade()
print(f"New level of {raha.name}: {raha.level}")

print(f"\nInitial level and capacity of {kavir_mine.name}: Level {kavir_mine.level}, Capacity {kavir_mine.capacity}")
kavir_mine.upgrade()
print(f"New level and capacity of {kavir_mine.name}: Level {kavir_mine.level}, Capacity {kavir_mine.capacity}")


# STEP 5: Financial calculations

taha_base_income = taha.calc_income()
print(f"\nBase daily income for {taha.name}: {taha_base_income}")

taha_life_cost = taha.calc_life_cost()
print(f"Daily living cost for {taha.name}: {taha_life_cost}")

taha_net_daily = taha.calc()
print(f"Net daily financial status for {taha.name}: {taha_net_daily}")


mine_maintenance_cost = kavir_mine.calc_costs()
print(f"\nDaily maintenance cost for {kavir_mine.name}: {mine_maintenance_cost}")

mine_net_daily = kavir_mine.calc()
print(f"Net daily financial status for {kavir_mine.name}: {mine_net_daily}")

# STEP 5: General calculations

total_people_financial_status = Person.calc_all()
print(f"\nTotal daily financial status of all people: {total_people_financial_status}")

total_workplaces_financial_status = WorkPlace.calc_all()
print(f"Total daily financial status of all workplaces: {total_workplaces_financial_status}")

overall_economy_status = total_people_financial_status + total_workplaces_financial_status
print(f"Overall simulator economy status: {overall_economy_status}")
