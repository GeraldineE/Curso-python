from tkinter import *
from tkinter import messagebox
# Ventana principal 
# top = tkinter.Tk()
# top.mainloop()

# Botones
top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()