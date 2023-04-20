from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


def Next():
    global i
    i = i + 1
    try:
        image_label.config(image=lst[i])
    except:
        i = -1
        Next()


def Back():
    global i
    i = i - 1
    try:
        image_label.config(image=lst[i])
    except:
        i = 0
        Back()


window = Tk()
window.geometry("300x300+0+0")
# window.resizable(0,0)
window.title("TechVidan")
Label(window, text="Image Viewer App", font=("bold", 20)).pack()

frame = Frame(window, width=230, height=200, bg="white")
frame.pack()


Button(window, text="Back", command=Back, bg="light blue").place(x=230, y=40)
Button(window, text="Next", command=Next, bg="Light blue").place(x=1000, y=40)

image1 = ImageTk.PhotoImage(Image.open("image1.jpg"))
image2 = ImageTk.PhotoImage(Image.open("image2.jpg"))
image3 = ImageTk.PhotoImage(Image.open("image3.jpg"))

lst = [image1, image2, image3]
i = 0
image_label = Label(frame, image=lst[i])
image_label.pack()

mainloop()
