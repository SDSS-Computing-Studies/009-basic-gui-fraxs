import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.title("Example")
dogphoto = PhotoImage(file="dog.png")
Labeldogphoto = tk.Label(window,image=dogphoto)
label1 = tk.Label(window,text="Pochacco!")
label2 = tk.Label(window,text="A cuddly little puppy! This is from the same \ncreators who brought you Keropi and Kero Kero",background='#A3FFFF')


Labeldogphoto.grid(row = 1, column = 1, rowspan = 3, sticky=E)

label1.grid(row = 2, column = 2, sticky=W)
label2.grid(row = 5, column =1,columnspan = 2,)
window.mainloop()