import tkinter as tk
import tkinter.filedialog as tkfd
from tkinter.messagebox import showerror
import customtkinter as ctk
from PIL import Image, ImageTk
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

font_style_menu = ("Bookman Old Style", 15, "bold")
font_style_text1 = ("Bookman Old Style", 60, "bold")
font_style_text2 = ("Bookman Old Style", 30)

bg_fg_color = "#2b2b2b"
text_color = "#FFFFFF"
text_text1 = "Get started with Photos"
text_text2 = "Once you add photos, you'll be able to view them all here"


class ImageViewer:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("600x500+0+0")
        self.window.resizable(0, 0)
        self.window.title("CLARSEN: Image Viewer")

        self.menu_bar = self.create_menu_bar()
        self.frame_display = self.create_frame_display()
        self.label = self.create_label()

    def create_menu_bar(self):
        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Image...",
                              font=font_style_menu, command=self.create_open_image)
        file_menu.add_command(label="Open Folder...",
                              font=font_style_menu, command=self.create_open_folder)
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit", font=font_style_menu, command=self.window.quit)

    def create_frame_display(self):
        main_frame = ctk.CTkFrame(
            self.window, width=590, height=490, corner_radius=10, fg_color=bg_fg_color)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_label(self):
        text1 = tk.Label(self.frame_display, text=text_text1, font=font_style_text1,
                         background=bg_fg_color, foreground=text_color)
        text1.place(relx=0.5, rely=0.5, x=-500, y=-110)

        text2 = tk.Label(self.frame_display, text=text_text2, font=font_style_text2,
                         background=bg_fg_color, foreground=text_color)
        text2.place(relx=0.5, rely=0.5, x=-555, y=-20)

    def create_open_image(self):
        file_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
        open_image = tkfd.askopenfilename(filetypes=file_types)

        img = Image.open(open_image)
        img = img.resize((1175, 965), resample=Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)

        image_label = tk.Label(self.frame_display, image=img)
        image_label.image = img
        image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def next_image(self):
        try:
            next_one = list_images.curselection()
            next_one = next_one[0]+1
            image = list_images.get(next_one)
            img = Image.open(image)
            img = img.resize((1175, 965), resample=Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            image_label = tk.Label(self.frame_display, image=img)
            image_label.image = img
            image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            list_images.select_clear(0, tk.END)
            list_images.activate(next_one)
            list_images.selection_set(next_one, last=None)

            self.button_pre = ctk.CTkButton(
                self.frame_display, text="<", width=5, command=self.previous_image)
            self.button_pre.place(relx=0.5, rely=0.5, x=-295, y=-25)
            self.button_nex = ctk.CTkButton(
                self.frame_display, text=">", width=5, command=self.next_image)
            self.button_nex.place(relx=0.5, rely=0.5, x=275, y=-25)
        except:
            showerror("No Next Image", "Please, press the previous button.")

    def previous_image(self):
        try:
            next_one = list_images.curselection()
            next_one = next_one[0]-1
            image = list_images.get(next_one)
            img = Image.open(image)
            img = img.resize((1175, 965), resample=Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            image_label = tk.Label(self.frame_display, image=img)
            image_label.image = img
            image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            list_images.select_clear(0, tk.END)
            list_images.activate(next_one)
            list_images.selection_set(next_one, last=None)

            self.button_pre = ctk.CTkButton(
                self.frame_display, text="<", width=5, command=self.previous_image)
            self.button_pre.place(relx=0.5, rely=0.5, x=-295, y=-25)
            self.button_nex = ctk.CTkButton(
                self.frame_display, text=">", width=5, command=self.next_image)
            self.button_nex.place(relx=0.5, rely=0.5, x=275, y=-25)
        except:
            showerror("No Previous Image", "Please, press the next button.")
    #     next_one = self.listImages.curselection()
    #     next_one = next_one[0]-1
    #     image = self.listImages.get(next_one)
    #     self.img1 = Image.open(image)
    #     self.img1 = self.img1.resize(
    #         (1175, 965), resample=Image.Resampling.LANCZOS)
    #     self.img1 = ImageTk.PhotoImage(self.img1)
    #     self.imageLabel = tk.Label(self.frame_display)
    #     self.imageLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    #     self.imageLabel["compound"] = tk.LEFT
    #     self.imageLabel["image"] = self.img1

    #     self.listImages.select_clear(0, tk.END)
    #     self.listImages.activate(next_one)
    #     self.listImages.selection_set(next_one, last=None)
    #     self.var.set(Image)

    #     self.button_pre = ctk.CTkButton(
    #         self.frame_display, text="<", width=5, command=self.previous_image)
    #     self.button_pre.place(relx=0.5, rely=0.5, x=-295, y=-25)
    #     self.button_nex = ctk.CTkButton(
    #         self.frame_display, text=">", width=5, command=self.next_image)
    #     self.button_nex.place(relx=0.5, rely=0.5, x=275, y=-25)

    def create_open_folder(self):
        global list_images
        open_folder = tkfd.askdirectory()
        os.chdir(open_folder)
        all_images = os.listdir(open_folder)
        all_images.reverse()
        list_images = tk.Listbox(self.frame_display, bd=5, width=30, height=20)
        list_images.place(x=100, y=100)
        for image in all_images:
            pos = 0
            if image.endswith((".jpg", ".png")):
                list_images.insert(pos, image)
                pos += 1
        list_images.selection_set(0)
        list_images.see(0)
        list_images.activate(0)
        list_images.selection_anchor(0)
        image = list_images.curselection()
        images = list_images.get(image[0])
        img = Image.open(images)
        img = img.resize((1175, 965), resample=Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        image_label = tk.Label(self.frame_display, image=img)
        image_label.image = img
        image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.button_pre = ctk.CTkButton(
            self.frame_display, text="<", width=5, command=self.previous_image)
        self.button_pre.place(relx=0.5, rely=0.5, x=-295, y=-25)
        self.button_nex = ctk.CTkButton(
            self.frame_display, text=">", width=5, command=self.next_image)
        self.button_nex.place(relx=0.5, rely=0.5, x=275, y=-25)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    image_viewer = ImageViewer()
    image_viewer.run()
