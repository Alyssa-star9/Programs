# Practice with tkinter tabs
from tkinter import ttk
from tkinter import *

window = Tk()
window.title("Welcome")
window.geometry('500x300')

tab_control = ttk.Notebook(window)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')

lbl1_1 = Label(tab1, text='Label 1 on the First Tab')
lbl1_1.grid(row=0, column=0)
lbl2_1 = Label(tab2, text='Another Label, Second Tab')
lbl2_1.grid(row=0, column=0)

tab_control.pack(expand=1, fill='both')  # expand and fill the window
window.mainloop()  