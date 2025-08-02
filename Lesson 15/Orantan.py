def start_of_roblox():
    Roblox = input("Do you play Roblox? (yes/no)? ")
    if Roblox.upper() == "YES":
        print("That's great! Another question for you. ")
        Roblox2 = input("D you play Grow A Garden? (yes/no)")
        if Roblox2.upper() == "YES":
            print("Good")
            print("The more expensive the fruit the more beter the fruit")
            print("Save as much money as you can.")
            print("Sell your normal dogs and get money for better dogs and aim for the Oranatan")
            print("The features of the Oranatan are: ""\n 1. It is a gold egg creature. ""\n 2. It has a unique ability to produce rare fruits.""\n 3. It is a rare creature to get.""\n 4. It gives you free elder strawberries and dragon fruits.")
        else:
            print("Play it once and you will like it!")
    elif Roblox.upper() == "NO":
        print("Sorry but the game is for free. You can play it anytime. ")
    else:
        print("Please answer with yes or no. ")
        return start_of_roblox()
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

start_of_roblox()

print("Thank you")
from turtle import *
import time
wake = int(input("Enter the number of seconds to wake up: "))
time.sleep(wake*2)
print("You sleep for", wake, "seconds")