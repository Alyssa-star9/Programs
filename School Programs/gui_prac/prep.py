# This is just practice on how to run a GUI applications from tkinter.
from tkinter import *

window = Tk()
window.title("Welcome")

window.geometry('350x200')  # this sets the size of the window
# Create a label widget

# this sets position on the form
# lbl = Label(window, text = "Hello", width=20, font=("Arial Bold", 50))

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)  # grid is used to position the label in the window
btn = Button(window, text="Click Me", highlightbackground="purple") # creates a button
btn.grid(column=1, row=0)  # grid is used to position the button in the window


window.mainloop() # calls the main loop of the window, this is what keeps the window open