from tkinter import *
import os
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.messagebox import *


class Images(Frame):
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("1370x680+-10+10")
        self.root.resizable(width=1, height=1)
        self.root.configure(bg="gray72")

        files = "back.jpg"
        self.var = StringVar()
        self.var.set(files.title())
        self.namelabel = Label(self.root, textvariable=self.var, bd=2, fg="black",
                               bg="white", font="helvetica, 15 bold", relief="raised", width=50)
        self.namelabel.place(x=400, y=1)

        self.img1 = Image.open(files)
        self.img1 = self.img1.resize((1360, 640), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img1)
        self.imageLabel = Label(self.root)
        self.imageLabel.place(x=2, y=30)
        self.imageLabel["compound"] = LEFT
        self.imageLabel["image"] = self.img

        # 12:45


def main():
    root = Tk()
    ui = Images(root)
    root.mainloop()


if __name__ == "__main__":
    main()
