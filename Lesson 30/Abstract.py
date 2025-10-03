# imported the abc module and the abstractmethod decorator from it.
from abc import ABC, abstractmethod

#Create the base
class AbsClass(ABC):

    # Function to print value
    def print(self, x):
        print("Passed value :", x)
    
    # Abstract method
    @abstractmethod
    def task(self):
        print("We are inside the AbsClass Task Point")


# Create the inherited class (sub class)
class TestClass(AbsClass):
    def task(self):
        print("We are inside the Test Class Point")

# Object of the sub class(TestClass)
t = TestClass()
t.task()
t.print(10)