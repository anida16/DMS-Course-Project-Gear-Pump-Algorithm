# Code for Displaying Images in Tkinter
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

img = ImageTk.PhotoImage(Image.open(r"Transmission Unit.png"))
myLabel = Label(image=img)
myLabel.pack()

root.mainloop()
