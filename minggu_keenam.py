#Praktik ke -1

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
print("Total Perulangan: ", hitung)

#Praktik ke-2

count = 0
while(count < 100):
    print("Jumlah adalah: ", count)
    count = count + 1
print("Selamat tinggal")

#Praktik ke-3

ulang_str = input('Jumlah perulangan: ')
ulang = int(ulang_str)
for i in range(ulang):
    print('Perulangan ke-', i)

# Praktik ke-4

item = ['kopi', 'nasi', 'teh', 'jeruk']
for isi in item:
    print(isi)

# Praktik ke-5

i = 0
while(i < 5):
    j = 0
    while(j < 5):
        print("A", end="")
        j += 1
    print("B\t")
    i += 1
    
# Praktik ke-6

daftar_nilai = [80, 67, 75, 83, 90,65]
print(min(daftar_nilai))
print(max(daftar_nilai))
avg = sum(daftar_nilai) / len(daftar_nilai)
print(avg)