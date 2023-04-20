import tkinter as tk
import tkinter.filedialog as tkf
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
        self.frame_display_default = self.create_frame_display_default()
        self.label_default = self.create_label_default()
        # self.images_list = []
        # # # self.images_vars = []
        # self.images_list = []
        # self.images_vars = []

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

    def create_frame_display_default(self):
        main_frame = ctk.CTkFrame(
            self.window, width=590, height=490, corner_radius=10, fg_color=bg_fg_color)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_label_default(self):
        text1 = tk.Label(self.frame_display_default, text=text_text1, font=font_style_text1,
                         background=bg_fg_color, foreground=text_color)
        text1.place(relx=0.5, rely=0.5, x=-500, y=-120)

        text2 = tk.Label(self.frame_display_default, text=text_text2, font=font_style_text2,
                         background=bg_fg_color, foreground=text_color)
        text2.place(relx=0.5, rely=0.5, x=-555, y=-30)

    def create_open_image(self):
        open_image = tkf.askopenfilename()
        image = os.listdir(open_image)
        

    def create_open_folder(self):
        open_folder = tkf.askdirectory()
        folder = os.listdir(open_folder)
        # i=0
        # image_label = tk.Label(self.create_frame_display_photo, image=self.images_list[i])
        
        # for image in range(0, len(folder)):
        #     self.images_list.append(ImageTk.PhotoImage(Image.open(open_folder + "/" + self.images_list[image])))
            
        

    def create_frame_display_photo(self):
        main_frame = ctk.CTkFrame(
            self.window, width=590, height=490, corner_radius=10, fg_color=bg_fg_color)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    image_viewer = ImageViewer()
    image_viewer.run()
