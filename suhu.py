def konversi_suhu(C):
    """
    Fungsi Konversi Suhu - Karena hidup sudah panas, mari ukur seberapa panas
    Parameter: C (Celsius)
    Mengembalikan: F (Fahrenheit), R (Reaumur), K (Kelvin)
    """
    F = C * 9 / 5 + 32
    R = C * 4 / 5
    K = C + 273.15
    
    return F, R, K

def main():
    try:
        print("Program Konversi Suhu")
        print("-" * 50)
        
        C = float(input("Masukkan suhu dalam Celsius (C): "))
        F, R, K = konversi_suhu(C)
        
        print(f"\nHasil Konversi (Tadaa!):")
        print(f"Suhu Celsius: {C}°C")
        print(f"Suhu Fahrenheit: {F:.2f}°F (cara Amerika mengukur kepanasan)")
        print(f"Suhu Reaumur: {R:.2f}°R (cara kuno yang hampir dilupakan)")
        print(f"Suhu Kelvin: {K:.2f}K (cara saintis yang sok pintar)")
        
    except ValueError:
        print("Error: Aduh, itu bukan angka. Tolong masukkan angka yang benar.")

if __name__ == "__main__":
    main()
