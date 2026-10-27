from tkinter import Label, Tk
from time import strftime

root = Tk()
root.title("Digital Clock")
clock = Label(root, font=("Arial", 48), padx=20, pady=10)
clock.pack()


def update_clock():
    clock.config(text=strftime("%H:%M:%S"))
    root.after(1000, update_clock)


update_clock()
root.mainloop()