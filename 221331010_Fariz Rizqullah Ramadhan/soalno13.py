def cari_rata_rata(daftar_angka):
    jumlah_angka = 0
    for i in daftar_angka:
        jumlah_angka += i
    return jumlah_angka/len(daftar_angka)
print(cari_rata_rata([1, 2, 3, 4, 5])) # harus mencetak 3.0
print(cari_rata_rata([10, 20, 30])) # harus mencetak 20.0