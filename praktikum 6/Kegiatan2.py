## Program Akun
## Dibuat oleh Ilyas L200190179
import random
angka = random.randint(0,1000)

Nama = 'Ilyas Muhlisin'
TanggalLahir = '21 oktober 2001'
NamaSingkat = Nama[0] + '.' + Nama[6:14]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[11:15]
Password = Nama[0:3] + str(angka)
