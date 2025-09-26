class Game:
    def __init__(self):
        self.name = "Cricket"
        self.players = 11
        self.country = "India"
    def display(self):
        print("Game Name: ", self.name)
        print("Number of Players: ", self.players)
        print("Country: ", self.country)

game1 = Game()
game1.display()