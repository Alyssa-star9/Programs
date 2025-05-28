# This is just practice on how to run a GUI applications from tkinter.
from tkinter import *

def addMe():
    global counter # use counter from Main

    # res = "Welcome to " + txt.get()
    # lbl.configure(text = res) # if you click the button and there is text in the entry widget,
                              # it will show "Welcome to" concatenated with the entered text.
    counter += int(txt.get())
    lbl.configure(text = counter)

# Main Program
# global variables
counter = 0 # keeps track of something

window = Tk()
window.title("Welcome")
window.geometry('200x75')  # this sets the size of the window
# Create a label widget

# this sets position on the form
# lbl = Label(window, text = "Hello", width=20, font=("Arial Bold", 50))

lbl = Label(window, text="Hello")
lbl.grid(row=0, column=0)  # grid is used to position the label in the window

txt = Entry(window, width=10)
txt.grid(row=1, column=0)  # grid is used to position the entry box in the window

btn = Button(window, text="Add Me", command = addMe) # creates a button
btn.grid(row=1, column=1)  # grid is used to position the button in the window

txt.focus() # sets the cursor into the entry box so that you can type in it immediately

window.mainloop() # calls the main loop of the window, this is what keeps the window open