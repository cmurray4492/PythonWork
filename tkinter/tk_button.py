from tkinter import *

def display():
    print("Button clicked")

root = Tk()
root.geometry("300x400")

button = Button(root, text="Click Here", command=display)
button.pack()

root.mainloop()
