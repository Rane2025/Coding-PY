def start_of_roblox(Roblox, Roblox2):
    Roblox = input("Do you play Roblox? (yes/no)? ")
    if Roblox.upper() == "YES":
        print("That's great! Another question for you. ")
        Roblox2 = input("D you play Grow A Garden? (yes/no)")
        if Roblox2.upper() == "YES":
            print("Good")
            print("The more expensive the fruit the more beter the fruit")
            print("Save as much money as you can.")
            print("Sell your normal dogs and get money for better dogs and aim for the ranatan")
        else:
            print("Play it once and you will like it!")
    elif Roblox.upper() == "NO":
        print("Sorry but the game is for free. You can play it anytime. ")
    else:
        print("Please answer with yes or no. ")
        return start_of_roblox(Roblox, Roblox2)
    print("Thanks!")
import turtle

turtle.title("Orananton")
turtle.bgcolor("black")
turtle.pensize(50)
turtle.pencolor("red")
turtle.pendown()
turtle.forward(200)
turtle.right(250)
turtle.left(265)
turtle.back(500)
turtle.left(907)
turtle.right(907)
turtle.penup()
turtle.goto(0, 0)
start_of_roblox("Roblox", "Roblox2")