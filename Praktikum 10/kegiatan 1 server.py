import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print "program komunikasi tentang data diri"
data = ""
kamus = {"nama" : "Ilyas Muhlisin",
         "NIM" :"L200190179",
         "angkatan":"2019",
         "keluar":"siap!!"}
while data.lower() != "q":
    komm, addr = s.accept()
    while data.lower != "q":
        data = komm.recv(1024)
        print "perintah:", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("maaf,perintah tidak dimengrti")
                  
