class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary


class Mechanic(Employee):
    job_title = "Mechanic"

employees = [
    Employee("Vera", 2000),
    Employee("Chuck", 1800),
    Employee("Samantha", 1800),
    Employee("Roberto", 2100),
    Mechanic("Dave", 2200),
    Mechanic("Tina", 2300),
    Mechanic("Ringo", 1900)
]

for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")

