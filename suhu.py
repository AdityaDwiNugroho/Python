def konversi_suhu(suhu_celsius):
    """
    Fungsi Konversi Suhu - Karena hidup sudah panas, mari ukur seberapa panas
    Parameter: suhu_celsius (C - Celsius)
    Mengembalikan: suhu_fahrenheit (F), suhu_reaumur (R), suhu_kelvin (K)
    """
    suhu_fahrenheit = suhu_celsius * 9 / 5 + 32
    suhu_reaumur = suhu_celsius * 4 / 5
    suhu_kelvin = suhu_celsius + 273.15
    
    return suhu_fahrenheit, suhu_reaumur, suhu_kelvin

def main():
    try:
        print("Program Konversi Suhu")
        print("-" * 50)
        
        suhu_celsius = float(input("Masukkan suhu dalam Celsius (C): "))
        suhu_fahrenheit, suhu_reaumur, suhu_kelvin = konversi_suhu(suhu_celsius)
        
        print(f"\nHasil Konversi (Tadaa!):")
        print(f"Suhu Celsius: {suhu_celsius}°C")
        print(f"Suhu Fahrenheit: {suhu_fahrenheit:.2f}°F (cara Amerika mengukur kepanasan)")
        print(f"Suhu Reaumur: {suhu_reaumur:.2f}°R (cara kuno yang hampir dilupakan)")
        print(f"Suhu Kelvin: {suhu_kelvin:.2f}K (cara saintis yang sok pintar)")
        
    except ValueError:
        print("Error: Aduh, itu bukan angka. Tolong masukkan angka yang benar.")

if __name__ == "__main__":
    main()
