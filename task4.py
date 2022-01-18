import tkinter as tk
window = tk.Tk()
window.title("Example")
dogphoto = tk.PhotoImage(file="dog.png")
Labeldogphoto = tk.Label(window,image=dogphoto)
label1 = tk.Label(window,text="Pochacco!")
label2 = tk.Label(window,text="A cuddly little puppy! This is from the same \ncreators who brought you Keropi and Kero Kero",background='#A3FFFF')

Labeldogphoto.place(x = 60, y = 0)
label1.place(x = 130, y = 50)
label2.place(x = 0, y = 100)
window.geometry("260x150")
window.mainloop()