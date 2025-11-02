from tkinter import *
from datetime import date

root= Tk()
root.title("Get started with widgets")
root.geometry("400x300")

lbl = Label(root, text="Welcome to Tkinter!", font=("Pixel Light", 20))
nlbl = Label(text="Full name",bg='magenta')
name_entry = Entry()

def display():
    name= name_entry.get()
    global message
    message = "Welcome to this application! \nToday's date is: "
    greet = "Hello, " + name + "\n"


    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="Submit",
command = display, height=1, bg='lightblue', fg='red')

lbl.pack()
nlbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()