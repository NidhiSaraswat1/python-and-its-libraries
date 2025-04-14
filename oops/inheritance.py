# inheritance is inheriting multiple parent classes in a child class
# thi si also called as multiple inheritance


class Employee():
    company = "ITC"
    name ="NIdhi"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

class coder():
    language ="python"
    salary = 120000000000
    def printlanguage(self):
     print(f"your language is {self.language}")


class programmer(Employee, coder):
    company="ITC Infotech"
    def showlanguages(self):
       print(f"the company name is {self.company} and the language is {self.language}")




a = Employee()
b = programmer()
b.show()
b.showlanguages()
b.printlanguage()
# print(a.company, b.company)        
   