# Soal Responsi: Hitung Nilai Akhir
# Follow github: https://github.com/AdityaDwiNugroho
# 讲师：Firman Asharudin, S.Kom., M.Kom

print("\n--- Program Hitung Nilai Akhir by Aditya Dwi Nugroho NIM 25.01.5252---")
try:
    nilai_kuis = float(input("Masukkan nilai Kuis: "))
    nilai_kehadiran = float(input("Masukkan nilai Kehadiran: "))
    nilai_responsi1 = float(input("Masukkan nilai Responsi 1: "))
    nilai_responsi2 = float(input("Masukkan nilai Responsi 2: "))
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))

    rata_responsi = (nilai_responsi1 + nilai_responsi2) / 2
    
    nilai_akhir = (0.2 * nilai_kuis) + (0.1 * nilai_kehadiran) + (0.2 * rata_responsi) + (0.25 * nilai_uts) + (0.25 * nilai_uas)

    print(f"\nNilai Akhir: {nilai_akhir:.2f}")

    if nilai_akhir >= 60:
        print("Status: LULUS")
    else:
        print("Status: TIDAK LULUS")

except ValueError:
    print("Input tidak valid!")
