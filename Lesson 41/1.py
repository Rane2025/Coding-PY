# Import nessacary libraries
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Settingup main window
root = Tk()
root.title("Denominator Visualizer")
root.configure(bg="#6b7ede")
root.geometry("650x400")

# Add Image and labels in the main loop
upload = Image.open("app_main.jpg")

# Resize the image by using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)


lable1 = Label(
    root,
    text = "Hey User! Welcome to Denominator Visualizer",
    bg = "#5fbedb",

)
lable1.place(relx = 0.5, y = 0.1, anchor=CENTER)

# Function to display messagebox and proceed if OKN  is clicked
def msg_box():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate denomination counts?"
    )
    if MsgBox == "ok":
        topwin()
    
# Adding Buttons to the main window
button1 = Button(
    root,
    text="Let's get started",
    command = msg_box,
    bg="#a95c19ff",
    fg="#ffffff"
)
button1.place(x = 260, y = 360)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denomination Visualizer")
    top.geometry("650x400")
    top.configure(bg="#6b7ede")

    lable2 = Label(
        top,
        text = "Enter the amount to be calculated:",
        bg = "#5fbedb",
    )
    lable2.place(relx = 0.5, y = 50, anchor=CENTER)

    entry1 = Entry(top, width=30)
    entry1.place(relx = 0.5, y = 100, anchor=CENTER)

    button2 = Button(
        top,
        text="Calculate",
        bg="#a95c195d",
        fg="#ffffff"
    )
    button2.place(relx = 0.5, y = 150, anchor=CENTER)
    top.mainloop()

