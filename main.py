class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = [
    Employee("Vera", 2000),
    Employee("Chuck", 1800),
    Employee("Samantha", 1800),
    Employee("Roberto", 2100),
    Employee("Dave", 2200),
    Employee("Tina", 2300),
    Employee("Ringo", 1900),
    Employee("Wendy", 2000)
]

for e in employees:
    if e.name == "Vera":
        print(f"{e.name}, ${e.salary}, Manager")
    if e.name == "Chuck" or e.name == "Samantha":
        print(f"{e.name}, ${e.salary}, Attendant")
    if e.name == "Roberto":
        print(f"{e.name}, ${e.salary}, Cook")
    if e.name == "Dave" or e.name == "Tina" or e.name == "Ringo":
        print(f"{e.name}, ${e.salary}, Car Repair")

