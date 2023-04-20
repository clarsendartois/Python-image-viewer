from tkinter import * 
from guizero import *


#background can be set rgb values,color name, and hex values
# width and height set the defualt startup window size
app=App(title='Test',bg=(53, 60, 81),width=500,height=500)

#sets min and max size of window
app.tk.minsize(width=250,height=250)
app.tk.maxsize(width=550,height=550)

root = app.tk


#Basic test function
def hello():
    print ("hello!")
    
    
        
    
#creates the menubar and sets the location to root window
menubar = Menu(root,relief=FLAT,bd=0)


'''
bg sets the menubar background color
fg sets the text color
activebackground sets the selected item background
activeforeground set the selected item text color
active borderwidth removes the 3d effect/border around item
font sets the font type and size
Defualt text,background and other things can be set with variables

'''

menubar.config(bg = "GREEN",fg='blue',activebackground='red',activeforeground='purple',activeborderwidth=0,font=("Verdana", 12))


# create a pulldown menu, and add it to the menu bar
# background,foreground and bother border and active border width needs to be set to remove any 3d border effect
filemenu = Menu(menubar, tearoff=0,relief='flat', bd=0,activebackground='red',activeborderwidth=0,font=("Verdana", 12))
filemenu.config(bg = "GREEN") 
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Save", command=hello)
#add line between drop down menu items
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
# sets the top level menu list name
menubar.add_cascade(label="File", menu=filemenu)





# create a pulldown menu, and add it to the menu bar
#example of no styling added to the sub menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
# sets the top level menu list name
menubar.add_cascade(label="Edit", menu=editmenu)

# create a pulldown menu, and add it to the menu bar
# show custom effects can be add to each sub menu 
helpmenu = Menu(menubar, tearoff=0,bg='orange')
helpmenu.add_command(label="Report bug", command=hello)
helpmenu.add_command(label="About", command=hello)
# sets the top level menu list name
menubar.add_cascade(label="Help", menu=helpmenu)




# example of guizero widget
box = Box(app,height=200,width=500)
box.set_border(thickness=2, color='green')
box.bg=(53, 60, 81)
box.text_color='white'
exampel_text = Text(box, text="Hello World")
Picture(box,"example.png")


# display the menu and other things
root.config(menu=menubar)
app.display()