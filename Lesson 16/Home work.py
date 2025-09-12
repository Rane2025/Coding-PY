users = {
    "Rosana52": "Rosana",
    "Mewtue76": "Mewtue",
    "Rane2025": "Rane",
    "Splash55": "Splash"
}

# ...existing code...

def send_message_v1():
    sender = input("Enter your username: ")
    if sender not in users:
        print("Sender not found. Please login or sign up first.")
        return
    recipient = input("Enter recipient's username: ")
    if recipient not in users:
        print("Recipient not found.")
        return
    message = input("Enter your message: ")
    print(f"Message from {sender} to {recipient}: {message}")

# After login or sign up, ask if the user wants to send a message
a = int(input("Enter 1 for login or 2 for sign up: "))
if a == 1:
    Masenger_Login()
elif a == 2:
    Masenger_SignUp()
else:
    print("Invalid!")

send = input("Do you want to send a message? (yes/no): ")
if send.lower() == "yes":
    send_message_v1()

def Masenger_Login():
    username = input("Welcome to Masenger since 2025, please enter your user name: ")
    if username in users:
        print("Welcome back to Masenger, " + username + "!")
    else:
        print("User not found, please try again.")

def Masenger_SignUp():
    username = input("Create a new username: ")
    if username in users:
        print("Username already exists. Please choose another.")
    else:
        name = input("Enter your name: ")
        users[username] = name
        print(f"User {username} signed up successfully!")

a = int(input("Enter 1 for login or 2 for sign up: "))
if a == 1:
    Masenger_Login()
elif a == 2:
    Masenger_SignUp()
else:
    print("Invalid!")

# ...existing code...

def send_message():
    sender = input("Enter your username: ")
    if sender not in users:
        print("Sender not found. Please login or sign up first.")
        return
    recipient = input("Enter recipient's username: ")
    if recipient not in users:
        print("Recipient not found.")
        return
    message = input("Enter your message: ")
    print(f"Message from {sender} to {recipient}: {message}")

# After login or sign up, ask if the user wants to send a message
a = int(input("Enter 1 for login or 2 for sign up: "))
if a == 1:
    Masenger_Login()
elif a == 2:
    Masenger_SignUp()
else:
    print("Invalid!")

send = input("Do you want to send a message? (yes/no): ")
if send.lower() == "yes":
    send_message()