# Import necessary librarys
from tkinter import *
# Create Window
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

# Event Handler for keypress
def keypress_handler(event):
    print(event.char)

# Bind the keypress event to the handler
window.bind("<KeyPress>", keypress_handler)

# Event handler from click button
def handle_click(event):
    print("\nThe button was clicked!")

# Create Button
button = Button(window, text="Click Me")
button.pack()

# Bind the button click event to the handler
button.bind("<Button-1>", handle_click)

# Start the GUI event loop
window.mainloop()