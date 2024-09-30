from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic

employees = [
    Manager("Vera", "Schmidt", 2000),
    Attendant("Chuck", "Norris", 1800),
    Attendant("Samantha", "Carrington", 1800),
    Cook("Roberto", "Jacketti", 2100),
    Mechanic("Dave", "DreiBig", 2200),
    Mechanic("Tina", "River", 2300),
    Mechanic("Ringo", "Rama", 1900),
    Mechanic("Chuck", "Rainey", 1800)
]


def print_accounting_report():
    print("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.first_name} {e.last_name}, ${e.salary}")

def print_staffing_report():
    print("Staffing")
    print("========")
    for e in employees:
        print(f"{e.first_name} {e.last_name}, {e.job_title}")


print_accounting_report()
print()
print_staffing_report()

