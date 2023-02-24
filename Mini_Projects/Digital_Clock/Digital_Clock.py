from tkinter import Tk   ##pip install Tk
from tkinter import Label   #pip install Label
import time


root = Tk()   #Tk(). It helps to display the root window and manages all the other components of the tkinter application
root.title("Clock")

def present_time():
    display_time = time.strftime("%d-%m-%y\n%I: %M : %S %p")

    Digi_Clock.config(text= display_time)
    Digi_Clock.after(150, present_time)
Digi_Clock = Label(root, font=("Comic Sans", 55), bg="Black", fg="White")
Digi_Clock.pack()

present_time()

root.mainloop()
