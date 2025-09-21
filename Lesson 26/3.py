class Parrot:
    species = "bird"
    def __init__(self, name , age):
        self.name=name
        self.age=age

Shrink = Parrot("Shrink", 15)
Sharky = Parrot("Sharky", 10)
print("Shrink is", Shrink.species, "and is", Shrink.age, "years old")
print("Sharky is", Sharky.species, "and is", Sharky.age, "years old")

print(f"{Shrink.name} is {Shrink.age} years old")
print(f"{Sharky.name} is {Sharky.age} years old")

buy = input("Do you want to buy a parrot?(y/n)")

if buy == "y":
    price = int(input("Enter the price your price to buy the parrot: "))
    if price >= 1000:
        parrot = input("Which")