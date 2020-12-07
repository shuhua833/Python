from tkinter import *

window = Tk()

window.title("Welcome to my first code")

lbl = Label(window)

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Happy Birthday to you !!",font=("Times", 50))

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=700, row=70)

window.mainloop()
