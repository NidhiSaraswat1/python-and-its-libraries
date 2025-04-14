class Employee():
    a=1 
    @classmethod #now it will print class attribute instead of instance attribute. it uses cls as objectninstead of self
    def show(cls):
        print(f"the value of a is {cls.a}")

e = Employee()
e.a = 45
e.show()        