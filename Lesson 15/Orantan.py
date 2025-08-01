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
start_of_roblox("Roblox", "Roblox2")
