# import necessary packages
from abc import ABC, abstractmethod
# Create the base class
class Animal(ABC):

    # Abstract method
    # Should be implemented in the sub class
    def move(self):
        pass

# sub class
class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()

# Question

ask = input("Who am I?")
if ask == "All Animals":
    print("I am a Human, Snake, Dog and Lion")
    print("Correct")
else:
    print("Wrong Answer")