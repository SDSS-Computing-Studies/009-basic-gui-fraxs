import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()

window.title("tk")

entry1 = tk.Entry(window, text="Entry widgets can be typed in")
label1 = tk.Label(window, text="x")
entry2 = tk.Entry(window, text="Entry bruh")
label2 = tk.Button(window, text="=")
entry3 = tk.Entry(window, text="")

entry1.pack(side=LEFT)
label1.pack(side=LEFT)
entry2.pack(side=LEFT)
label2.pack(side=LEFT)
entry3.pack(side=LEFT)

window.mainloop()