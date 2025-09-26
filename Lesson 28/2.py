class Person:
        def __init__(self, name, idnumber):
            self.name = name
            self.idnumber = idnumber
        def display(self):
            print("Name:", self.name)
            print("ID Number:", self.idnumber)

class Employee(Person):
        def __init__(self, name, idnumber, salary, post):
            self.salary = salary
            self.post = post
            Person.__init__(self, name, idnumber)
        def display(self):
            Person.display(self)
            print("Salary:", self.salary)
            print("Post:", self.post)

a = Employee("Franza", 886012, 23689400, "Science Engineer")
a.display()

