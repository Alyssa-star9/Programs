# This is an attempt at the GUI for Math Flash Cards game.
# Note that this may be discarded later and is not yet a complete version of the game.

from tkinter import ttk
from tkinter import *

# Define the function to switch tabs
def btn_1to2():
    tab_control.select(tab2)
def btn_2to3():
    tab_control.select(tab3)

# Main Window
window = Tk()
window.title("Math Flash Cards")
window.geometry('1024x768')

# Create a Notebook (tab control)
tab_control = ttk.Notebook(window)
# Create tabs
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)
tab_control.add(tab1, text='Welcome')
tab_control.add(tab2, text='Settings')
tab_control.add(tab3, text='Start Game')

# Create labels for the tabs
intro = Label(tab1, text='Welcome to the Math Flash Cards Game!', font=("Times New Roman", 25))
intro.grid(row=0, column=0, padx=280, pady=20) # Moves the label to different position on the tab

# Create buttons to switch tabs

# switch1 = Button(tab1, text='Go to Settings', command=btn_1to2, font=("Arial", 15))
# switch1.grid(row=1, column=0, padx=10, pady=10)  # Places the button on the first tab
# switch2 = Button(tab2, text='Start Game', command=btn_2to3, font=("Arial", 15))
# switch2.grid(row=1, column=0, padx=10, pady=10)  # Places the button on the second tab

# Pack the tab control
tab_control.pack(expand=1, fill='both')

# Settings Tab

window.mainloop()


