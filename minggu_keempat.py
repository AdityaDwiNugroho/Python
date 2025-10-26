# Fungsi Input
nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama: ")
print("NIM: ", nim, "Tipe Data: ", type(nim))
print("Nama: ", nim, "Tipe Data: ", type(nama))


# Fungsi output
a = "X"
b = 15
c = 3.14
d = False
print("Penggunaan Separator", 50*"=")
print("a=", a, 'b=', b, 'c=', c, 'd=', d, sep='@')
print('Penggunaaan Akhiran Karakter', 50*'=', end=' ')
print('Hello Boy')


#Character escape
kalimat = "Saya makan bakso nih"
frase = "di Warung"
hasil = kalimat + '\t' + frase # operasi concatenation
print(hasil)

#Fungsii format
nama = 'Aditya'
nim = '5252'
uang = 1439000
kalimat = 'Nama saya adalah {0}. Saya memiliki NIM {1}.\n Saya memiliki uang {2:,} di bank'.format(nama, nim, uang)
print(kalimat)