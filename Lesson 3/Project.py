# You have ? Robuxs in your Roblox account.
# You need to withdraw some money for Robux.
# This project will extract money and tell how much Robux you must get.
#  If you already have some Robux, you can add it in the total amount. If you don't have any Robux, you can tupe 0.
print("You have 0 Robux in your Roblox account.")
Robux_already_have = int(input("How much Robux do you have?"))

#  To withdraw money for Robux (main part)
print("This is just an app that will help you decide how much Robux you can get.")
Robux_need = int(input("How much money do you want to withdraw for Robux? (in dollars) "))

#  To define the data (main part)
robux_rate = 80  # Example: 1 dollar = 80 Robux
robux_gained = Robux_need * robux_rate

print("You will get", robux_gained, "Robux for your money you withdrew.")

#  To find the total Robux you must code like this: (main part)
Total_Robux = robux_gained + Robux_already_have
print("You will have", Total_Robux, "Robux in your Roblox account after you withdraw your money.")

#  To find the average Robux you must code like this: (main part)
average_Robux = Total_Robux / 2  # Average of old and new Robux
print("The average Robux you will have is", average_Robux, "Robux.")

#  It ends right here. Enjoy your Roblox time and have fun!
print("It ends right here. Enjoy your Roblox time and have fun!")