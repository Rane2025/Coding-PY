# Import necessary librarys
from tkinter import *
from tkinter import messagebox


# Setup Tikinter window
root = Tk()
root.geometry("200x200")

# Function to handle button click event
def msg():
    messagebox.showwarning("Alert", "Stop! Virus found!")

# Add Button widget to window 
button = Button(root, text="Click Me", command=msg)
button.pack(pady=50)

# entering main event loop
root.mainloop()