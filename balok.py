# Menghitung volume dan luas permukaan balok
# Rumus:
p = int(input("Masukkan panjang balok (p): "))
l = int(input("Masukkan lebar balok (l): "))
t = int(input("Masukkan tinggi balok (t): "))

choice = input("Mau ngitung apa nih? Volume, luas permukaan, atau jumlah rusuk? (v/s/k): ")
print("=========================")

if choice == "v":
    V = p * l * t
    print("Volume baloknya adalah: ", V, "... Wah gede juga ya!")
elif choice == "s":
    L = 2 * (p * l + l * t + t * p)
    print("Luas permukaannya: ", L, "... Buset luas bener!")
elif choice == "k":
    K = 4 * (p + l + t)
    print("Jumlah rusuknya: ", K, "... Lumayan banyak juga!")
else:
    print("Hmm, inputnya tidak valid. Tolong pilih v, s, atau k saja ya!")

print("=========================")