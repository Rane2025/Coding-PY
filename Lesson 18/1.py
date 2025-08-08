import random
playing = True
number = str(random.randint(10, 20))

print("I will generate a number between 10 and 20. ")
print("The game ends when you get one hero.")
while playing:
    guess = input("Give me your best guess: \n")
    if guess == number:
        print("You guessed it! The number was ", number)
        break
    else:
        print("Sorry, that's not correct. The answer was", number)