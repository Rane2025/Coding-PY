class Buses():
    def __init__(self, Ride_price, Max_speed, Milage):
        self.Ride_price = Ride_price
        if Max_speed >= 200:
            self.Max_speed = 200
        else:
            self.Max_speed = Milage

class Taxi(Buses):
    def Bus_info(self, speed):
        speed = int(input("Choose the taxi speed: (max 500)"))
        self.Max_speed = 500
        if speed > self.Max_speed:
            print("The speed is too high")
        else:
            print("The speed is ok")
        print("$" + str(speed))

Sans_car_taxi = Taxi(2.5, 500, 20)
Sans_car_taxi.Bus_info(500)
class Truck(Buses):
    def Truck_info(self, weight):
        weight = int(input("Enter the weight of the truck: (max 10000)"))
        self.weight = 10000
        if weight > self.weight:
            print("The weight is too high")
        else:
            print("The weight is ok")
        print(str(weight) + "kg") 
Sans_car_truck = Truck(4.5, 200, 15)
Sans_car_truck.Truck_info(10000)