from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic

employees = [
    Manager("Vera", 2000),
    Attendant("Chuck", 1800),
    Attendant("Samantha", 1800),
    Cook("Roberto", 2100),
    Mechanic("Dave", 2200),
    Mechanic("Tina", 2300),
    Mechanic("Ringo", 1900)
]


def print_accounting_report():
    print("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.name}, ${e.salary}")

print_accounting_report()

