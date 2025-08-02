a = int(input("Enter 1 for login or 2 for sighn up: "))
if a == 1:
    def Masenger_SignUp():
        a = input("Welcome to Masenger since 2025, please enter your user name: ")
elif a == 2 :
    def Masenger_Login():
        b = input("Welcome to Masenger since 2025, please enter your user name: ")
        if b == "Rosana52" or b == "Mewtue76" or b == "Rane2025":
            print("Welcome back to Masenger, " + b + "!")
        else:
            return "User not found, please try again."
else:
    print("Indvalid!")
