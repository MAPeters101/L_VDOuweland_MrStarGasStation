class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.last_name}, {self.first_name}"

class Manager(Employee):
    job_title = "Manager"

class Cook(Employee):
    job_title = "Cook"

class Attendant(Employee):
    job_title = "Station Attendant"

class Mechanic(Employee):
    job_title = "Mechanic"