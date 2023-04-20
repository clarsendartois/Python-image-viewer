from tkinter import *

root = Tk()
root.title("Codemy.com - Learn To Code!")
# root.iconbitmap("c:/gui/codemy.ico")
root.geometry("400x400+0+0")


# click command
def our_command():
    pass


my_menu = Menu(root)
root.config(menu=my_menu)

# Create a menu item
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# # Create an edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)

# # Create an edit menu item
test_menu = Menu(my_menu)
my_menu.add_cascade(label="Test", menu=test_menu)


root.mainloop()
