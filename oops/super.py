# super is for inheriting constructor in child class
class Employee():
    def __init__(self) :
        print("constructor of employee")
    a = 10

class Programmer(Employee):
    def __init__(self) :
        print("constructor of programmer")
    
    b = 20

class Manager(Programmer):
    def __init__(self) :
        super().__init__()
        print("constructor of manager")
    
    c = 30

# e = Employee()
# print(e.a)    # here b and c will show error

# p = Programmer()
# print(p.a,p.b)   #here c will show error

m = Manager()
print(m.a,m.b,m.c)  #no error as employee is inherited by programmer