# Continuation of prep1.py
from tkinter.ttk import Combobox
from tkinter import *

def clicked():
    lbl.configure(text = combo.get())

# Main Program
window = Tk()
window.title("Welcome")
window.geometry('350x200')

# create combo box
combo = Combobox(window)
combo['values'] = [1,2,3,4,5, "Text"] # adds values as a list
combo.current(1) # set the selected item
combo.grid(row=0, column=0)

lbl = Label(window) # adds empty Label to window
lbl.grid(row=1, column=0, sticky=W) # align text to West (left) side

bttn = Button(window, text="Press Me", command = clicked)
bttn.grid(row=2, column=0) 

window.mainloop()