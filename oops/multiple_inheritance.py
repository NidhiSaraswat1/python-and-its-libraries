# multiple im=nheritance is when child class is further inherited by other child classes
class Employee():
    a = 10

class Programmer(Employee):
    b = 20

class Manager(Programmer):
    c = 30

e = Employee()
print(e.a)    # here b and c will show error

p = Programmer()
print(p.a,p.b)   #here c will show error

m = Manager()
print(m.a,m.b,m.c)  #no error as employee is inherited by programmer