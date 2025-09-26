class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage 

class Bus(Vehicle):
    pass

school = Bus("School Volvo", 180, 12)
print("Vehicle Name:", school.name, "Speed:", school.max_speed, "Mileage:", school.mileage)