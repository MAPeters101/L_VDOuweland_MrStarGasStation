from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport
from reporting import ScheduleReport
import datetime

employees = [
    Manager("Vera", "Schmidt", 2000, datetime.time(8,00), datetime.time(14,00)),
    Attendant("Chuck", "Norris", 1800, datetime.time(8,00), datetime.time(14,00)),
    Attendant("Samantha", "Carrington", 1800, datetime.time(12,00), datetime.time(20,00)),
    Cook("Roberto", "Jacketti", 2100, datetime.time(8,00), datetime.time(14,00)),
    Mechanic("Dave", "DreiBig", 2200, datetime.time(8,00), datetime.time(14,00)),
    Mechanic("Tina", "River", 2300, datetime.time(8,00), datetime.time(14,00)),
    Mechanic("Ringo", "Rama", 1900, datetime.time(12,00), datetime.time(20,00)),
    Mechanic("Chuck", "Rainey", 1800, datetime.time(12,00), datetime.time(20,00))
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees)
]

for r in reports:
    r.print_report()
    print()
