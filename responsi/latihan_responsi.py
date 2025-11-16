i = 0

while i < 5:
    j = 0
    while j < 5:
        if j == i:
            print("@", end=" ")
        else:
            print("\t", end=" ")
        j += 1
    print()
    i += 1
    
    
    
# No 2

print('Menampilkan faktor dari bilangan: ')
nilai = int(input('Bilangan: '))
print(f'Faktor dari bilangan {nilai} adalah: ')
for i in range(1, nilai + 1):
        hasil = nilai % i
        if (hasil == 0):
            print(i, end=',')
            
# No 3

total_belanja = int(input("input total belanja: "))
jumlah_kupon = total_belanja / 20000
print(int(jumlah_kupon))

# No 4

bilangan = int(input("Input bilangan: "))

prima = True

if bilangan <= 1:
    prima = False
else:
    for i in range(2, bilangan):
        if bilangan % i == 0:
            prima = False
            break
        
if prima:
    print("ini bilangan prima")
else:
    print("ini bukan bilangan prima")
    
# No 5

for i in range(4):
    for j in range(4):
        if i == j:
            print("@", end=" ")
        elif i + j == 3:
            print("#", end= " ")
        else:
            print("*", end=" ")
    print()