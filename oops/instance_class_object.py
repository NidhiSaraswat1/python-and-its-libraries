class Employee:

    language ="python"
    salary =2000000000

#    it is importsnt to give self even if you are not gonna use it in program
    def getinfo(self):
        print(f"the language is {self.language},the salary is {self.salary}")


    # to not give self arguement make it  a static method
    @staticmethod   
    def greet():
        print("hello world!")


# harry is an an object here
harry = Employee()
# instance attribute get preference over class object
harry.language = "javascript"
print(harry.language, harry.salary)


# harry.getinfo()
Employee.getinfo(harry)
harry.greet()