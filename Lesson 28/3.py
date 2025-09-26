class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def super_power(self):
        print("Fly faster")
        print("Swims faster")
    
class Pelican(Bird):
    def __init__(self):
        super().__init__()
        print("Pelican is ready")
    
    def whoisThis(self):
        print("Pelican")

    def speak(self, message):
        print(message)
Pelican1 = Pelican()
Pelican1.whoisThis()
Pelican1.super_power()
Pelican1.speak("Squawk Squawk")