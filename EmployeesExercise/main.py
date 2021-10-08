from employees import Employees
from accounting import Accounting
from engineering import Engineering


emp1 = Accounting('sarah', 'marshall', 554113313, 'smarshall@company.com', 'CA', 800_000)
emp2 = Engineering('sipho', 'dlomo', 2116483154, 'sdlomo@company.com', 'Solutions Architect', 745_000, 'Rivonia, Sandton' )
emp3 = Accounting('mike', 'jones', 687468418, 'jonesm@company.com', 'Manager', 980_000, 'Centurion, Pretoria')
emp4 = Engineering('yolisa', 'sizani', 894615231, 'ysizani@company.com', 'software engineer', 600_000)

emp1.changeEmail('sarah.marshall@company.com')
emp1.displayInfo()
emp2.displayInfo()
emp3.displayInfo()
emp4.displayInfo()