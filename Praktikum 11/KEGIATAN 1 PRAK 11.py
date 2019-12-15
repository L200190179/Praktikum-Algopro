from tkinter import Tk,Label,Entry,Button
from tkinter import messagebox

my_app = Tk(className = "Data Diri")

L = Label(my_app, text="Data Diri", font = ("Arial",24))
L.grid(row = 0, column = 0, sticky="w")

L1 = Label(my_app, text = "Nama")
L1.grid(row = 1, column = 0, sticky="w")

L2 = Label(my_app, text = "Ilyas Muhlisin")
L2.grid(row = 1, column = 1, sticky="w")

L3 = Label(my_app, text = "NIM")
L3.grid(row = 2, column = 0, sticky="w")

L4 = Label(my_app, text = "L200190179")
L4.grid(row = 2, column = 1, sticky="w")

L5 = Label(my_app, text = "Buku favorit")
L5.grid(row = 3, column = 0, sticky="w")

L6 = Label(my_app, text = "Harry potter")
L6.grid(row = 3, column = 1, sticky="w")

L7 = Label(my_app, text = "Idola")
L7.grid(row = 4, column = 0, sticky="w")

L8 = Label(my_app, text = "Muhammad SAW")
L8.grid(row = 4, column = 1, sticky="w")

L9 = Label(my_app, text = "Motto")
L9.grid(row = 5, column = 0, sticky="w")

L10 = Label(my_app, text = "buatlah bangga orang tua")
L10.grid(row = 5, column = 1, sticky="w")

def keluar():
    my_app.destroy()
    messagebox.showinfo("Pesan", "Terima kasih.")
    
B = Button(my_app, text = "Tutup", command = keluar)
B.grid(row = 6, column = 1)

my_app.mainloop()
