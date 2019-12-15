from tkinter import *
from tkinter import messagebox

my_app = Tk()
my_app.title('Judul Aplikasi')

L0 = Label(my_app, text="Bangun Geometri", font=("Arial", 16))
L0.grid(row=0, column=0, sticky="W")

DESC = Label(my_app, text="prisma adalah bangun ruang tiga dimensi yang dibatasi oleh alas dan tutup identik berbentuk segi-n dan sisi-sisi tegak berbentuk persegi atau persegi panjang. Dengan kata lain prisma adalah bangun ruang yang mempunyai penampang melintang yang selalu sama dalam bentuk dan ukuran. Prisma segi-n memiliki n + 2 sisi, 3n rusuk dan 2n titik sudut..", wraplength=250)
DESC.grid(row=1, sticky="W")

DIMENSI  = Label(my_app, text="prisma segitiga merupakan geometri tiga dimensi")
DIMENSI.grid(row=2, sticky="W")

CONTOH = Label(my_app, text="Contoh geometri prisma segitiga adalah atap rumah")
CONTOH.grid(row=3, sticky="W")

L3 = Label(my_app, text = "Alas")
L3.grid(row = 4, column = 1, sticky = "w")

alas = IntVar()
E3 = Entry(my_app, textvariable = alas)
E3.grid(row = 4, column = 2)

L3 = Label(my_app, text = "Tinggi")
L3.grid(row = 5, column = 1, sticky = "w")

tinggi = IntVar()
E3 = Entry(my_app, textvariable = tinggi)
E3.grid(row = 5, column = 2)

L3 = Label(my_app, text = "Panjang")
L3.grid(row = 6, column = 1, sticky = "w")

panjang = IntVar()
E3 = Entry(my_app, textvariable = panjang)
E3.grid(row = 6, column = 2)

L3 = Label(my_app, text = "Lebar")
L3.grid(row = 7, column = 1, sticky = "w")

lebar = IntVar()
E3 = Entry(my_app, textvariable = lebar)
E3.grid(row = 7, column = 2)

H = Label(my_app, text = "Luas")
H.grid(row = 8, column = 1, sticky = "w")

H1 = Label(my_app)
H1.grid(row = 8, column = 2, sticky = "w")

def Hitung():
    hasil = 3*panjang.get()*lebar.get()+alas.get()*tinggi.get()

    H1.config(text = hasil)

B1  = Button(my_app, text = "Hitung", width = "8", command = lambda:Hitung())
B1.grid(row = 9, column = 2)
