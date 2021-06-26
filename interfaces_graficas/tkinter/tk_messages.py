from tkinter import *

root = Tk()

var = StringVar()
label = Message( root, textvariable = var, relief = RAISED )

var.set("Hey? Ultimos temas en el ciclo")
label.pack()
root.mainloop()