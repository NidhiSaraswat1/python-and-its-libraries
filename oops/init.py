class Employee:
    language ="python"
    salary =2000000000

# init is a dunder method which is automatically called
    def __init__(self, name, salary,language) :
        self.name = name
        self.salary = salary
        self.language = language                            
        print("i am creating an object") 
        

    def getinfo(self):
        print(f"the language is {self.language},the salary is {self.salary}")


    @staticmethod   
    def greet():
        print("hello world!")

harry = Employee("nishi", 13000000000, "python")
# harry.name = "Nidhi"
print(harry.name, harry.salary, harry.language)        