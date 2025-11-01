# Made by Aditya Dwi Nugroho - Minggu Kelima

# Pernyataan Kondisi
nilai = 79

if nilai > 80:
    print("A")
elif nilai > 60:
    print("B")
elif nilai > 40:
    print("C")
elif nilai > 20:
    print("D")
else:
    print("Balik TK aja lu")



# Praktik ke-1

nilai = 9
if (nilai > 7):
    print("Selamat anda dinyatakan Lulus")


if (nilai > 10):
    print("Selamat anda dinyatakan Lulus")

# Praktik ke-2
umur = int(input("Masukkan angka: "))
if umur >= 18:
    print("Anda sudah beranjak dewasa")
else:
    print("Anda masih dibawah umur")

# Praktik ke-3
print("Masukkan sebuah angka...")
print("Dan Anda akan check hubungna kedua angka tersebut")
angka1 = input("Masukkan angka pertama: ")
angka1 = int(angka1)
angka2 = input("Masukkan angka kedua: ")
angka2 = int(angka2)


if angka1 == angka2:
    print(angka1, "sama dengan", angka2)
else:
    print(angka1, "tidak sama dengan", angka2)


# Praktik ke-4
gaji = int(input("Masukkan gaji: "))
berkeluarga = bool(int(input("Masukkan 0/1: ")))
punya_rumah = input("Masukkan yes/no: ")
punya_rumah = punya_rumah.lower()
if gaji > 3000000:
    print("gaji sudah diatas UMR")
    if berkeluarga:
        print("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print("Tidak perlu ikutan asuransi")
    if punya_rumah == "yes" or punya_rumah == "ya" or punya_rumah == "y" or punya_rumah == "iya" or punya_rumah == "ye":
        print("Wajib bayar pajak rumah")
    else:
        print("Tidak wajib bayar pajak rumah")
else:
    print("Gaji lu belum UMR BOSS Kerja yang giat")


# Praktik ke-5
hari_ini = "Minggu"

if(hari_ini == "Senin"):
    print("Saya kuliah")
elif(hari_ini == "Selasa"):
    print("Saya kuliah")
elif(hari_ini == "Rabu"):
    print("Saya kuliah")
elif(hari_ini == "Kamis"):
    print("Saya kuliah")
elif(hari_ini == "Jumat"):
    print("Saya kuliah")
elif(hari_ini == "Sabtu"):
    print("Saya tidak kuliah")
elif(hari_ini == "Minggu"):
    print("Saya tidur")
else:
    print("Input tidak valid")