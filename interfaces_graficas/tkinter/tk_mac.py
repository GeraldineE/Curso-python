from tkinter import Tk
from tkmacosx import Button

root = Tk()
root.geometry('200x150')
B0 = Button(root, text='Button')
B0.pack(padx=20, pady=(20,0))
B1 = Button(root, text='Button', bg='#ADEFD1',
            fg='#00203F', borderless=1)
B1.pack(padx=20, pady=10)
B2 = Button(root, text='Button', bg='#E69A8D',
            fg='#5F4B8B', borderless=1,
            activebackground=('#AE0E36', '#D32E5E'),
            activeforeground='#E69A8D')
B2.pack()
root.mainloop()