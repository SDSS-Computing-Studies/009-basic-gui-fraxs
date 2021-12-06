import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
SearchByName = tk.Button(window,text="Search by Name")
SBNentry = tk.Entry(window, text='')
ClientDatabase = tk.Label(window,text="Client Database")
dogphoto = PhotoImage(file="dog.png")
labelName =  tk.Label(window,text="Name")
labelType = tk.Label(window,text="Type")
labelBreed = tk.Label(window,text="Breed")
labelOwner = tk.Label(window,text="Owner")
labelBDate = tk.Label(window,text="Birthdate")
entryName = tk.Entry(window,text="")
entryType = tk.Entry(window,text="")
entryBreed = tk.Entry(window,text="")
entryOwner = tk.Entry(window,text="")
entryBdate = tk.Entry(window,text="")
labelDogphoto = tk.Label(window,image=dogphoto)


labelDogphoto.grid(row = 1, column = 1)
SBNentry.grid(row = 2, column = 2)


window.mainloop()