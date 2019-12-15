from tkinter import Tk,Label,Entry,Button,IntVar
from tkinter import messagebox

my_app = Tk(className = "Kalkulator Sederhana")

L = Label(my_app, text = "Angka 1")
L.grid(row = 0, column = 0, sticky="w")

angka1 = IntVar()
E = Entry(my_app, textvariable = angka1)
E.grid(row = 0, column = 1, columnspan = 3)

L1 = Label(my_app, text = "Angka 2")
L1.grid(row = 1, column = 0, sticky="w")

angka2 = IntVar()
E1 = Entry(my_app, textvariable = angka2)
E1.grid(row = 1, column = 1, columnspan = 3)

H = Label(my_app, text = "Hasil")
H.grid(row = 3, column = 0, sticky="w")

H1 = Label(my_app)
H1.grid(row = 3, column = 2, sticky="w")

def Hitung(op):
    if op == '+':
        hasil = angka1.get()+angka2.get()
    elif op == '-':
        hasil = angka1.get()-angka2.get()
    elif op == 'x':
        hasil = angka1.get()*angka2.get()
    elif op == ':':
        hasil = angka1.get()/angka2.get()

    H1.config(text = hasil)

B1 = Button(my_app, text = "+", width="8", command = lambda:Hitung('+'))
B1.grid(row = 2, column = 0)

B2 = Button(my_app, text = "-", width="8", command = lambda:Hitung('-'))
B2.grid(row = 2, column = 1)

B3 = Button(my_app, text = "x", width="8", command = lambda:Hitung('x'))
B3.grid(row = 2, column = 2)

B4 = Button(my_app, text = ":", width="8", command = lambda:Hitung(':'))
B4.grid(row = 2, column = 3)

my_app.mainloop()
